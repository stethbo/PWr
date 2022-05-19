from numpy import *
from matplotlib.pyplot import*

# parametry symulacji
T = 250
h = 0.1

# parametry modelu

sigma = 10
b = 8/3
r = 28
war_pocz_x, war_pocz_y = 0.7, 0.3

t = arange(0, T, h)

x = zeros(t.shape)
y = zeros(t.shape)

x[0] = war_pocz_x
y[0] = war_pocz_y

for i in range(t.size-1):
    x[i+1] = x[i]+h*(a - b*y[i])*x[i]
    y[i+1] = y[i]+h*(c*x[i] - d)*y[i]