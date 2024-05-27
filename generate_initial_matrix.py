import numpy as np
from bezier_aproximation import bezier_curve

def generate_initial_matrix_with_bezier(nx, ny, p):
    # Generate Bezier curve
    x, y = bezier_curve(nx, p)

    # Initialize variables with Bezier curve values
    U = np.tile(y, (nx, 1)).T   #Repeat y ny times and transpose
    V = np.ones((ny, ny))
    P = np.zeros((nx, ny))
    
    return U, V, P
