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

    RU, RV, RP = navier_stokes_residuals(U_init, V_init, P_init, nu, dx, dy, dt, rho)
    print("Residuals for U:", RU)
    print("Residuals for V:", RV)
    print("Residuals for P:", RP)

    plt.plot(RV[:, 0], label='U_initial')
    plt.plot(RU[:, 0], label='V_initial')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Initial Approximation with Bezier Curve')
    plt.legend()
    plt.grid(True)
    plt.show()

# This block ensures that main() is called only when the script is executed directly
if __name__ == "__main__":
    main()
