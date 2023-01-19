import matplotlib.pyplot as plt
import multiprocessing as mp
import numpy as np
import random


size = 20
INTERVAL = 0.5
L = np.random.randint(0, 100, size)
X = np.arange(size)

def heap_sort_global(l):
    def heapify(arr, n, i):
        largest = i # Ustawienie największego jako ojciec
        l = 2 * i + 1	 # lewy syn = 2*i + 1
        r = 2 * i + 2	 # prawy syn = 2*i + 2

        # Sprwdzamy czy lewy syn istnieje
        # i jest większy od ojca
        if l < n and arr[largest] < arr[l]:
            largest = l

        # Sprwdzamy czy prawy syn istnieje
        # i jest większy od ojca
        if r < n and arr[largest] < arr[r]:
            largest = r

        # Zmiana ojca jeśli spełniony jest warunek
        if largest != i:
            
            arr[i], arr[largest] = arr[largest], arr[i] # swap

            plt.bar(X, arr)
            plt.title('Sortowanie przez kopcowanie')
            plt.pause(INTERVAL)
            plt.clf()


            # ponowne wywołanie kopcowania
            heapify(arr, n, largest)


    def heapSort(arr):
        n = len(arr)

        # Budowanie największego kopca
        for i in range(n//2 - 1, -1, -1):
            heapify(arr, n, i)

        # ektrakcja elementów
        for i in range(n-1, 0, -1):

            arr[i], arr[0] = arr[0], arr[i] # zamiana

            plt.bar(X, arr)
            plt.title('Sortowanie przez kopcowanie')
            plt.pause(INTERVAL)
            plt.clf()

            heapify(arr, i, 0)

    heapSort(l)



def quic_sort_global(array):
    def quicksort(arr, start, stop):
        if(start < stop):
            pivotindex = partitionrand(arr,start, stop)
            quicksort(arr , start , pivotindex)
            quicksort(arr, pivotindex + 1, stop)


    def partitionrand(arr , start, stop):
        randpivot = random.randrange(start, stop)
        arr[start], arr[randpivot] = arr[randpivot], arr[start]
        plt.bar(X, arr)
        plt.title('Quicksort - sortowanie szybkie')
        plt.pause(INTERVAL)
        plt.clf()
        return partition(arr, start, stop)
 

    def partition(arr,start,stop):
        pivot = start
        i = start - 1
        j = stop + 1
        while True:
            while True:
                i = i + 1
                if arr[i] >= arr[pivot]:
                    break
            while True:
                j = j - 1
                if arr[j] <= arr[pivot]:
                    break
            if i >= j:
                return j
            arr[i] , arr[j] = arr[j] , arr[i]
            plt.bar(X, arr)
            plt.title('Quicksort - sortowanie szybkie')
            plt.pause(INTERVAL)
            plt.clf()
            
    quicksort(array, 0, len(array) - 1)
    
    return array


if __name__ == '__main__':
    
    task1 = mp.Process(target=heap_sort_global, args=(L,))
    task2 = mp.Process(target=quic_sort_global, args=(L,))

    task1.start()
    task2.start()

    plt.show()