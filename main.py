from solution_plotting import plot_3d
from bezier_aproximation import bezier_curve
import numpy as np
import matplotlib.pyplot as plt
from initial_aproximation_generation import generate_initial_matrix_with_bezier_curve
from generate_initial_matrix import generate_initial_matrix_with_bezier
from newton_approximation import newton_raphson
from apply_boundaries_conditions import apply_boundary_conditions
from interpolations import interpolar_splines_bicubicos, interpolar_bilineal, interpolar_spline_orden_superior

def main():

    # Create a sample rectangular matrix
    #bezier_aproximation = generate_initial_matrix_with_bezier_curve()
    #plot_3d(bezier_aproximation)

    nx, ny = 50, 5  # Grid size  
    p = 0.5  # Bezier curve 
    nu, dx, dy, dt, rho = 0.1, 1.0/nx, 1.0/ny, 0.01, 1.0  # Parameters
    # Generate initial approximation using Bezier curve
    U_init, V_init = generate_initial_matrix_with_bezier(nx, ny, p)

    apply_boundary_conditions(U_init) 

    print("x: %s  -- y: %s" % (U_init, V_init))

    U = newton_raphson(U_init, V_init, nu, dx, dy, dt, rho)

    #Iterpolations for resulting matrix
    int_U = interpolar_splines_bicubicos(U)
    #interpolar_bilineal(U)
    # interpolar_spline_orden_superior(U)"""
   
    plot_3d(int_U)


# This block ensures that main() is called only when the script is executed directly
if __name__ == "__main__":
    main()
