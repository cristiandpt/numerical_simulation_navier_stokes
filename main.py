from solution_plotting import plot_3d
from bezier_aproximation import bezier_curve
import numpy as np

def main():

    # Create a sample rectangular matrix

    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ])

    plot_3d(matrix)
    # Print the results
    print("Hola desde el main")

# This block ensures that main() is called only when the script is executed directly
if __name__ == "__main__":
    main()
