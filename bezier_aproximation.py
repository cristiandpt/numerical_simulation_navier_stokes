import numpy as np

def bezier_curve(n, p):
    """
    Generate a Bezier curve that decays from 1 to 0 in n steps with a curvature parameter p.
    
    Parameters:
    n (int): Number of steps.
    p (float): Curvature parameter between 0 and 1.
    
    Returns:
    tuple: Arrays representing the x and y coordinates of the curve.
    """
    t = np.linspace(0, 1, n)
    x = t
    y = (1 - t)**3 * 1.0 + 3 * (1 - t)**2 * t * p + 3 * (1 - t) * t**2 * (1 - p) + t**3 * 0.0
    return x, y
