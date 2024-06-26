import numpy as np
from apply_boundaries_conditions import apply_boundary_conditions

def gauss_seidel(A, b, x0=None, tol=1e-10, max_iterations=1000):

    n = len(b)
    if x0 is None:
        x0 = np.zeros_like(b)
    
    x = x0.copy()

    apply_boundary_conditions(A)
    
    for k in range(max_iterations):
        x_old = x.copy()
        
        for i in range(n):
            if A[i, i] == 0:
                print("Zero diagonal element detected at index %s, matrix is singular or ill-conditioned." % i)
                raise ValueError(f"Zero diagonal element detected at index {i}, matrix is singular or ill-conditioned.")
            
            sigma = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x_old[i+1:])
            x[i] = (b[i] - sigma) / A[i, i]
        
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            break
    
    return x
