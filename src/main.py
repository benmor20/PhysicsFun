from matplotlib import pyplot as plt
import matplotlib.animation as anim
from matplotlib.collections import PatchCollection
import numpy as np


FPS = 60
DTIME = 1 / FPS


fig, ax = plt.subplots(figsize=(5, 5))
dot = plt.Circle((0, 0), radius=0.5, linewidth=0)
ax.add_patch(dot)
ax.grid()


def init():
    ax.set_ylim(0, 25)
    ax.set_xlim(0, 25)


def run(data):
    dot.center = data, 2 * data


def get_animation():
    return anim.FuncAnimation(fig, run, np.arange(0, 10, DTIME), interval=10, init_func=init)
