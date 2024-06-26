import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_3d(matrix):
    """
    Plotting the numerical solution in a 3D plot.

    Parameters:
    matrix (np.array): The array to be plotted in z axis.

    Returns:
    None
    
    Examples:
    >>> plot_3d(
      np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
      ])
    )
    """

    # Create the x and y coordinates
    x = np.arange(matrix.shape[1])
    y = np.arange(matrix.shape[0])
    x, y = np.meshgrid(x, y)

    # Create the figure and the 3D axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the surface
    ax.plot_surface(x, y, matrix, cmap='viridis')

    # Add labels
    ax.set_xlabel('Velocidad horizontal')
    ax.set_ylabel('Velocidad vertical')
    ax.set_zlabel('Velocidad instantanea')

    # Show the plot
    plt.show()
