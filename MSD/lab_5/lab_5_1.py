#  Zadanie 1 Model SIR
#  S' = -beta * I * S
#  I' = beta * I * S - gamma * I
#  R' = gamma * I

from matplotlib.pyplot import*
from scipy.integrate import odeint
from numpy import *


def model_sir(y, t, beta=0.2, gamma=0.1):
    S, I, R = y
    dt = [(-beta * I * S/40), (beta * I * S/40 - gamma * I), (gamma * I)]
    return dt


# parametry symulacji
t_min = 0
t_max = 100
dt = 0.1

t = np.arange(t_min, t_max, dt)
X = odeint(model_sir, (40, 1, 0), t)

t = linspace(0, 100, 1000)

fig = figure()
ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t, X[:, 0], 'red', label='S')
ax.plot(t, X[:, 1], 'blue', label='I')
ax.plot(t, X[:, 2], 'y-', label='R')

show()
