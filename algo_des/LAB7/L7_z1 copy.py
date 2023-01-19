import numpy as np


VECTOR = list(np.random.randint(100, 1000, 100))
print(VECTOR)

def quick_sort_asc(arr, low, high):
        if low > high or low < 0:
            return
        
        p, arr =  partition_asc(arr, low, high)

        quick_sort_asc(arr, low, p - 1)
        quick_sort_asc(arr, p + 1, high)

        return arr


def partition_asc(arr, low, high):
    piv = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= piv:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    
    i += 1
    arr[i], arr[high] = arr[high], arr[i]
    
    return i, arr

def quick_sort_desc(arr, low, high):
    if low > high: # or high >= len(arr):
        return
    
    p, arr =  partition(arr, low, high)

    quick_sort_desc(arr, low, p - 1)
    quick_sort_desc(arr, p + 1, high)

    return arr


def partition(arr, low, high):
    piv = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] >= piv:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    
    i += 1
    arr[i], arr[high] = arr[high], arr[i]
    
    return i, arr
    
def sort_vector(vec):
    l = len(str(max(vec))) # sprawdzenie ile cyfr ma ajwiększa liczba z listy
    prefixes = list()
    for n in range(l, 1, -1):
        prefixes.append([i * 10 ** (n-1) for i in range(10 ** (l - n + 1)  + 1)])

    rev = 1
    vec = quick_sort_asc(vec, 0, len(vec) - 1)

    for pref in prefixes:

        for p in range(len(pref) - 1):

            temp = [v for v in vec if (v >= pref[p] and v < pref[p+1])]
            if len(temp):
                low = vec.index(temp[0])
                high = vec.index(temp[-1])
                if rev:
                    temp = quick_sort_desc(temp, 0, len(temp) - 1)                    
                else:
                    temp = quick_sort_asc(temp, 0, len(temp) - 1)


                #temp = sorted(temp, reverse=rev)
                vec[low:high + 1] = temp

        if rev:
            rev = 0
        else:
            rev = 1
    return vec
        


V_NEW = sort_vector(VECTOR)
print('\nPOSORTOWANA LISTA:')
print(V_NEW)

with open('wynik_1.txt', 'w') as f:
    for line in V_NEW:
        f.write(str(line) + '\n')