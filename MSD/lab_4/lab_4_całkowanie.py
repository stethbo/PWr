# Całkowanie wbudowane w pythona
import matplotlib.pyplot as plt
from numpy import *
from matplotlib.pyplot import*
from scipy.integrate import odeint


def F(x, t):
    dx =[0, 0]
    dx[0] = x[1]
    dx[1] = -x[0]-0.5*x[1]
    return dx


# parametry symulacji
t_min = 0
t_max = 20
h = 0.01
t = np.arange(t_min, t_max, h)

# parametry RÓWNANIA RÓŻNICZKOWEGO

init_x = (1, 0)

X = odeint(F, init_x, t)

plt.subplot(1, 2, 1)
plt.plot(t, X[:, 0], label='całka 1')
plt.plot(t, X[:, 1], label='całka 2')
plt.ylabel('Y-etykieta')
plt.xlabel('X-etykieta')
plt.legend()
plt.title('Tytuł')

plt.subplot(1, 2, 2)
plt.plot(X[:, 0], X[:, 1], label='całka')
plt.ylabel('Y-etykieta')
plt.xlabel('X-etykieta')
plt.title('Tytuł')
plt.legend()
plt.show()
