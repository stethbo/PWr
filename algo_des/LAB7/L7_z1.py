import numpy as np


VECTOR = list(np.random.randint(100, 1000, 100))
print(VECTOR)

    
def sort_vector(vec):
    l = len(str(max(vec))) # sprawdzenie ile cyfr ma ajwiększa liczba z listy
    prefixes = list()
    for n in range(l, 1, -1):
        prefixes.append([i * 10 ** (n-1) for i in range(10 ** (l - n + 1)  + 1)])

    rev = 1
    vec = sorted(vec)

    for pref in prefixes:

        for p in range(len(pref) - 1):

            temp = [v for v in vec if (v >= pref[p] and v < pref[p+1])]
            if len(temp):
                low = vec.index(temp[0])
                high = vec.index(temp[-1])
                temp = sorted(temp, reverse=rev)                   
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