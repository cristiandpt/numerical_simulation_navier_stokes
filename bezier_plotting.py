import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.colorbar import ColorbarBase


def plotting_bezier_curves(matrix, x, y):
    """
    Plot the Bezier curve given the beziered matrix x and y intervals 
    """
    scale = Normalize(vmin=asinh_scale(x.min()), vmax=asinh_scale(x.max()))

    fig, ax = plt.subplots()
    c = ax.pcolormesh(matrix, norm=scale, cmap='viridis')

    ax.set_xlabel(r'$v_y~~donde~~v_{y_i} = 0$')
    ax.set_ylabel(r'$v_x~~donde~~v_{x_0} = 1$')

    cbar = plt.colorbar(c, ax=ax)
    cbar.set_label(r'$\frac{dv}{dt}$')

    plt.show()
