from solution_plotting import plot_3d
from bezier_aproximation import bezier_curve
import numpy as np
import matplotlib.pyplot as plt
from initial_aproximation_generation import generate_initial_matrix_with_bezier_curve
from navier_stokes_residuals import navier_stokes_residuals
from generate_initial_matrix import generate_initial_matrix_with_bezier

def main():

    # Create a sample rectangular matrix
    #bezier_aproximation = generate_initial_matrix_with_bezier_curve()
    #plot_3d(bezier_aproximation)

    nx, ny = 50, 50  # Grid size
    p = 0.5  # Bezier curve 
    nu, dx, dy, dt, rho = 0.1, 1.0/nx, 1.0/ny, 0.01, 1.0  # Parameters
    # Generate initial approximation using Bezier curve
    U_init, V_init, P_init = generate_initial_matrix_with_bezier(nx, ny, p)

    print("U_init: ", U_init)

    # Print the results
    print("Hola desde el main")

# This block ensures that main() is called only when the script is executed directly
if __name__ == "__main__":
    main()
