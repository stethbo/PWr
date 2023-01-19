import cmath
import math
import numpy as np
import matplotlib.pyplot as plt
"""implementacja wzoru z wikipedii"""
def fft(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1)) #k od 0.. do N
    e = np.exp(-2j * np.pi * k * n / N)/N


    X = np.dot(e, x)
    # print(k)

    return X



def showDft(X):

    # calculate the frequency
    N = len(X)
    n = np.arange(N)
    sr=1000
    T = N / sr
    freq = n / T


    plt.plot(freq, abs(X))
    plt.xlabel('freq')
    plt.ylabel("amplit")
    plt.show()


"""Tworzę sygnał"""
signal=[]
for i in range(100):
    signal.append(3*math.sin(10*i)+1/2*math.sin(2*i)+5*math.sin(5*i))

plt.plot(signal)
plt.title("sygnal")
plt.xlabel("czas")
plt.ylabel("amplituda")
plt.show()
res=fft(signal)
showDft(res)
newres=res


for i in range(22): #nakladam filr 210 z lewej i prawej
    newres[i]=0
    newres[-i]=0
showDft(newres)

s = np.fft.ifft(newres) #robie odwrotna transformate
# plt.plot(invDFT(res))
plt.plot(np.real(s)*100) #np.real zwraca rzezywista czes liczby zespolone
plt.xlabel("czas")
plt.ylabel("amplituda")

plt.show()

