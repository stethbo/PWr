import matplotlib.pyplot as plt
from numpy import *
from matplotlib.pyplot import*
from mpl_toolkits.mplot3d import Axes3D


def lorentz(x, y, z, sigma=10, b=8/3, r=28):
    dt_x = sigma * y - sigma * x
    dt_y = (-1 * x * z) + (r * x) - y
    dt_z = ((x * y) - (b * z))
    return dt_x, dt_y, dt_z


# parametry symulacji
T = 3000
dt = 0.01
sigma = 10
b = 8/3
r = 28

t = arange(0, T, dt)

x = []
y = []
z = []

x.append(0)
y.append(0.5)
z.append(1)

for i in range(T-1):
    x.append(x[i] + dt*sigma * (y[i] - x[i]))
    y.append(y[i] + dt*((-1 * x[i] * z[i]) + (r * x[i]) - y[i]))
    z.append(z[i] + dt*(x[i]*y[i] - b*z[i]))

fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
show()
