from matplotlib import pyplot as plt
import matplotlib.animation as anim
import numpy as np


FPS = 60
DTIME = 1 / FPS


fig, ax = plt.subplots()
line, = ax.plot([], [], 'ro')
ax.grid()
xdata, ydata = [], []


def init():
    ax.set_ylim(0, 50)
    ax.set_xlim(0, 50)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,


def run(data):
    global xdata, ydata
    xdata = [data]
    ydata = [2 * data]
    line.set_data(xdata, ydata)


def get_animation():
    return anim.FuncAnimation(fig, run, np.arange(0, 10, DTIME), interval=10, init_func=init)
