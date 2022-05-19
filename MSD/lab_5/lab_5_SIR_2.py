#  Zadanie 1 Model SIR
#  S' = -beta * I * S/n
#  I' = beta * I * S - gamma * I - mu*I
#  R' = gamma * I
#  D' = mu * I
#  N - ogólna populacja = S + I + R + D

from matplotlib.pyplot import*
from scipy.integrate import odeint
from numpy import *
import numpy as np


def model_sir(y, t, beta=0.2, gamma=0.1, mu=0.02):
    S, I, R, D = y
    dt = [(-beta * I * S/(S + I + R + D)), (beta * I * S/(S + I + R + D) - gamma * I - mu*I), (gamma * I), (mu*I)]
    return dt


# parametry symulacji
t_min = 0
t_max = 100
dt = 0.1

t = np.arange(t_min, t_max, dt)
X = odeint(model_sir, (40, 1, 0, 0), t)

t = linspace(0, 100, 1000)

fig = figure()
ax = fig.add_subplot(111, axisbelow=True)
ax.plot(t, X[:, 0], 'b', label='S')
ax.plot(t, X[:, 1], 'y-', label='I')
ax.plot(t, X[:, 2], 'g', label='R')
ax.plot(t, X[:, 3], 'black', label='D')

show()


