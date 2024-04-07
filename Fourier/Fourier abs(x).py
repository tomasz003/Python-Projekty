import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def cosine_fourier(n):  # Specifically pre-counted for f(x)=|x|
    if n%2==1:
        return -4/(n**2*np.pi)*np.cos(n*x)
    else:
        return 0


def update(frame):
    line.set_ydata(functions[frame])  # Update the y data of the plot
    return line,


x=np.linspace(-np.pi, np.pi, 100)
f=abs(x)

functions=[np.pi/2+x*0]

new_f=functions[0]

for i in range (1,15):
    new_f=new_f+cosine_fourier(i)
    functions.append(new_f)


fig, ax = plt.subplots()

# Initialize the plot line that will be updated
ax.plot(x, f, label='f(x)=|x|', color='lightgrey')
line, = ax.plot(x, functions[0], color="#19a6d1")

# Create an animation
ani = FuncAnimation(fig, update, frames=range(len(functions)), blit=True, interval=500)

# Plot customizing
plt.title("f(x)=|x| and its Fourier serie")
plt.gcf().patch.set_facecolor('#bde6f2')
plt.gca().set_facecolor('#050c1a')
plt.xlim(-3.3,3.3)
plt.ylim(-0.2,3.8)
plt.grid(True, linestyle='--', linewidth=0.5, color='lightgrey')
plt.legend()
plt.show()