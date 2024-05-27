import numpy as np

def gauss_seidel(A, b, x0=None, tol=1e-10, max_iterations=10):

    n = len(b)
    if x0 is None:
        x0 = np.zeros_like(b)
    
    x = x0.copy()
    
    for k in range(max_iterations):
        x_old = x.copy()
        
        for i in range(n):
            sigma = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x_old[i+1:])
            x[i] = (b[i] - sigma) / A[i, i]
        
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            break
    
    return x
