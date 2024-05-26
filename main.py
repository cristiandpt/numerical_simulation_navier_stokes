from solution_plotting import plot_3d
from bezier_aproximation import bezier_curve
import numpy as np
from initial_aproximation_generation import generate_initial_matrix_with_bezier_curve

def main():

    # Create a sample rectangular matrix
    bezier_aproximation = generate_initial_matrix_with_bezier_curve()
    plot_3d(bezier_aproximation)

    # Print the results
    print("Hola desde el main")

# This block ensures that main() is called only when the script is executed directly
if __name__ == "__main__":
    main()
