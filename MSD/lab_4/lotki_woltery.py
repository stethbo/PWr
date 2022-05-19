# Układ lotki woltery
import matplotlib.pyplot as plt
from matplotlib.pyplot import*
from scipy.integrate import odeint
import numpy as np

def lotki_wolteryu(y, t, a=.15, b=0.1, c=1.5, d=0.75):
    dx, dy = y
    dt = [(a - b*dy)*dx, (c*dx - d)*dy]
    return dt


# parametry symulacji
t_min = 0
t_max = 250
h = 0.01
t = np.arange(t_min, t_max, h)
X1 = odeint(lotki_wolteryu, (1, 1), t)

plt.subplot(2, 1, 1)
plt.plot(t, X1)
plt.subplot(2, 1, 2)
plt.plot(X1[:, 0], X1[:, 1])
plt.show()
