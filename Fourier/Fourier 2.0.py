import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import quad


def function(x):
    return a*x**4+b*x**3+c*x**2+d*x+e


def sin_fun(n,x):
    return function(x)*np.sin(n*x)


def sine_fourier(n):
    integral=quad(lambda x: sin_fun(n,x),-np.pi, np.pi)
    return 1/np.pi*integral[0]


def cos_fun(n,x):
    return function(x)*np.cos(n*x)


def cosine_fourier(n):
    integral=quad(lambda x: cos_fun(n,x),-np.pi, np.pi)
    return 1/np.pi*integral[0]


def update(frame):
    line.set_ydata(functions[frame])  # Update the y data of the plot
    return line,

# Defining f(x)
x=np.linspace(-np.pi, np.pi, 100)

print("f(x)=ax^4+bx^3+cx^2+dx+e")
a=float(input("a = "))
b=float(input("b = "))
c=float(input("c = "))
d=float(input("d = "))
e=float(input("e = "))


f=function(x)

#Series from 1 to i
new_f=cosine_fourier(0)/2+x*0
functions=[new_f]

for i in range (1,50):
    new_f=new_f+cosine_fourier(i)*np.cos(i*x)+sine_fourier(i)*np.sin(i*x)
    functions.append(new_f)

#Animating
fig, ax = plt.subplots()

ax.plot(x, f, label=f'f(x)={a}x^4+{b}x^3+{c}x^2+{d}x+{e}', color='lightgrey')
line, = ax.plot(x, functions[0], color="#19a6d1")

ani = FuncAnimation(fig, update, frames=range(len(functions)), blit=True, interval=200)

# Plot customizing
plt.title(f"f(x)={a}x^4+{b}x^3+{c}x^2+{d}x+{e} and its' Fourier serie")
plt.gcf().patch.set_facecolor('#bde6f2')
plt.gca().set_facecolor('#050c1a')
plt.xlim(-3.3,3.3)
plt.ylim(1.1*min(f)-1,1.1*max(f)+2)
plt.grid(True, linestyle='--', linewidth=0.5, color='lightgrey')
plt.legend()
plt.show()