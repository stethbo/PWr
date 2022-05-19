# Układ Lorentza
import matplotlib.pyplot as plt
from matplotlib.pyplot import*
from scipy.integrate import odeint


def lorentz(y, t, sigma=10, b=8/3, r=28):
    dx, dy, dz = y
    dxyz = [sigma*dy-sigma*dx, (-1*dx*dz)+(r*dx)-dy, ((dx*dy)-(b*dz))]
    return dxyz


# parametry symulacji
t_min = 0
t_max = 50
dt = 0.01

t = np.arange(t_min, t_max, dt)
X = odeint(lorentz, (1, 1, 1), t)

fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
ax.plot(X[:, 0], X[:, 1], X[:, 2], 'red')
show()
