import numpy as np
import matplotlib.pyplot as plt


def quick_sort(arr, low, high):
    if low > high: # or high >= len(arr):
        return
    
    p, arr =  partition(arr, low, high)

    quick_sort(arr, low, p - 1)
    quick_sort(arr, p + 1, high)

    return arr


def partition(arr, low, high):
    piv = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= piv:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

            plt.bar(X, arr)
            plt.pause(0.2)
            plt.clf()
    
    i += 1
    arr[i], arr[high] = arr[high], arr[i]
    plt.bar(X, arr)
    plt.pause(0.2)
    plt.clf()
    
    return i, arr

SIZE = 20
X = np.arange(SIZE)
L = np.random.randint(0, 1000, SIZE)
print(L)
quick_sort(L, 0, len(L) - 1)
print(L)

plt.show()