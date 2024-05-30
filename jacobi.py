import numpy as np

def jacobi(A, b, x0=None, tol=1e-10, max_iterations=100):
    n = len(b)
    if x0 is None:
        x0 = np.zeros_like(b)
    
    x = x0.copy()
    x_new = np.zeros_like(x)

    for k in range(max_iterations):
        for i in range(n):
            sigma = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - sigma) / A[i, i]
        
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            break
        
        x = x_new.copy()
    
    return x