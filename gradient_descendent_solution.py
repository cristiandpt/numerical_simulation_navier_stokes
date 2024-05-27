import numpy as np

def gradient_descent_system(funcs, jacobian, x0, learning_rate=0.01, tolerance=1e-6, max_iterations=1000):
    """
    Gradient descent algorithm to solve a system of equations.

    Parameters:
    funcs (list of functions): List of functions representing the system of equations.
    jacobian (function): Function to compute the Jacobian matrix.
    x0 (numpy array): Initial guess for the solution.
    learning_rate (float): Learning rate for the gradient descent updates.
    tolerance (float): Tolerance for convergence.
    max_iterations (int): Maximum number of iterations.

    Returns:
    numpy array: Solution vector.
    """
    x = x0
    for iteration in range(max_iterations):
        # Compute the residuals
        residuals = np.array([f(*x) for f in funcs])
        
        # Compute the Jacobian matrix
        J = jacobian(x)
        
        # Compute the gradient of the sum of squares of residuals
        gradient = 2 * J.T @ residuals
        
        # Update the solution
        x = x - learning_rate * gradient
        
        # Check for convergence

        if np.linalg.norm(gradient) < tolerance:
            print(f"Converged in {iteration} iterations")
            break
    
    return x

# Example usage with a system of 2 equations

# Define the system of equations
def f1(x1, x2):
    return x1**2 + x2**2 - 4

def f2(x1, x2):
    return x1 - x2 - 1

# Define the Jacobian matrix
def jacobian(x):
    x1, x2 = x
    return np.array([
        [2*x1, 2*x2],
        [1, -1]
    ])

# Initial guess
x0 = np.array([1.0, 1.0])

# List of functions
funcs = [f1, f2]

# Solve using gradient descent
solution = gradient_descendent_system(funcs, jacobian, x0)

print("Solution:", solution)
