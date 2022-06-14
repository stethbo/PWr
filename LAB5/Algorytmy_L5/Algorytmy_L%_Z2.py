import time
import numpy as np
import timeit
from math import sqrt
import matplotlib.pyplot as plt

def euklid(x,y): #implementacja jak w liscie
    if y == 0:
        return x
    return euklid(y,x%y)


def czp(number):
    res = []
    start = 2
    while start < sqrt(number):
        if number % start == 0:
            return czp(number // start) + czp(start)
        else:
            start += 1
    if res == []:
        return [number]

def aczp(x,y):
    c1=czp(x) #zbior dzielnikow dla 1 liczby
    c2=czp(y) #zbior dla 2
    res=1 #wynik tymczasowy
    for i in c1:
        if i in c2: #jezeli element z c1 jest w c2
            res*=i #mnozymy nasz wynik razy element ktory znalezlismy
            c2.remove(i) #i usuwamy go z c2
    return res

def mesureAndPlot(num,b):
    t1=[]
    t2=[]
    for i in range(b):
        start = time.time()
        euklid(num,i)
        end = time.time()
        t1.append(end-start)
        start = time.time()
        aczp(num, i)
        end = time.time()
        t2.append(end - start)
        if i %100000==0:
            print(i)

    plt.plot(t1)
    plt.title("sum Euklid = "+str(np.sum(t1)))
    plt.show()
    plt.plot(t2)
    plt.title("sum aczp = " + str(np.sum(t2)))
    plt.show()




'''rint(euklid(12,32))
print(euklid(15,24))
print(euklid(5,6))'''
print(aczp(6,12))
print(aczp(15,24))
print(aczp(5,6))

def indextonum(index):
    res=1
    while index>0:
        if index%10>0:
            res*=index%10
        index//=10
    return res
print(indextonum(508996))
print(0*5*8*9*9*6)
mesureAndPlot(indextonum(258996)*indextonum(260359), 100000)