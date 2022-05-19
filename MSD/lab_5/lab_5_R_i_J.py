'''  Zadanie 3 Model Romeo i Julii
R' = a * R + b * J
J' = c * R + d * J

Zbadać następujące przypadki
a>0 i b>0
b<0 i a>0 itd.

'''

from numpy import *
from matplotlib.pyplot import*

'''a = -0.15
d = 0.17
b = 0.9
c = -0.9'''


def romeo_i_julia(a, b, c, d):
    T = 14
    h = 0.5
    t = arange(0, T, h)
    r = zeros(t.shape)
    j = zeros(t.shape)
    r[0] = 1
    j[0] = -.5
    for i in range(t.size-1):
        r[i+1] = h * r[i] + a*r[i] + b*j[i]
        j[i+1] = h * j[i] + c*r[i] + d*j[i]

    x = linspace(0, 10, int(T/h))
    figure(1, figsize=(6, 4))
    plot(x, r)
    plot(x, j)
    show()


# romeo_i_julia(0.15, 0.17, 0.9, -0.9)
romeo_i_julia(.45, -.23, .8, -0.1)
