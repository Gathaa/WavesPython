import numpy as np
from numpy import pi 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.style.use('dark_background') 

wavelength=float(input("Enter Wavelength\n")) 
period=float(input("Enter The period T\n"))

fig = plt.figure()
fig.set_dpi(100)
ax1 = fig.add_subplot(1, 1, 1)

w= (2*pi)/period 
x0 = np.linspace(-pi, pi, 10000)
t0 = 0
dt = 0.05

def Wave(x, t): 
    return 1* (np.sin(2*pi*x/wavelength + w * t))

a = [] 

for i in range(500):
    value = Wave(x0, t0) 
    t0 = t0 + dt 
    a.append(value)
    k = 0

def animate(i): 
    global k
    x = a[k]
    k += 1 
    ax1.clear()
    plt.plot(x0, x, color='cyan') 
    plt.grid(True)
    plt.ylim([-2, 2])
    plt.xlim([-pi, pi])

anim = animation.FuncAnimation(fig, animate, frames=360, interval=20) 

plt.show()
