import numpy as np

"""
This is the python implementation of the Navier-Stokes equation discretized 
function defined by:

$u_{i,j} = \frac{u_{i+1,j} + u_{i-1,j} + u_{i,j+1} + u_{i,j-1} - \frac{u_{i+1,j}u_{i,j}}{2} + \frac{u_{i-1,j}u_{i,j}}{2} + \frac{u_{i,j-1}w_{i,j}}{2} - \frac{u_{i,j+1}w_{i,j}}{2}}{4}$

"""

def navier_stokes_discretized():
    """
    Calculates the discretized version of the Navier-Stokes equation at a given point (i, j) using the given velocity and pressure fields.

    Args:
        U (numpy.ndarray): The velocity field represented as a 2D array.
        W (numpy.ndarray): The pressure field represented as a 2D array.
        i (int): The row index of the point.
        j (int): The column index of the point.

    Returns:
        float: The discretized value of the Navier-Stokes equation at the given point.
    """
    return lambda U, W, i, j: (U[i+1, j] + U[i-1, j] + U[i, j+1] + U[i, j-1] -
            0.5 * U[i+1, j] * U[i, j] + 0.5 * U[i-1, j] * U[i, j] +
            0.5 * U[i, j-1] * W[i, j] - 0.5 * U[i, j+1] * W[i, j]) / 4

    
