import numpy as np
from computing_jacobian import compute_jacobian
from navier_stokes_residuals import navier_stokes_residuals

def newton_raphson(U, V, P, nu, dx, dy, dt, rho, tol=1e-6, max_iterations=100):

    for iteration in range(max_iterations):

        J = compute_jacobian(U, V, P, nu, dx, dy, dt, rho)
        RU, RV, RP = navier_stokes_residuals(U, V, P, nu, dx, dy, dt, rho)
        R = np.concatenate([RU.flatten(), RV.flatten(), RP.flatten()])
        
        if np.linalg.norm(R, ord=np.inf) < tol:
            print(f"Converged in {iteration} iterations")
            break
        
        delta = gauss_seidel(J, -R)
        
        nx, ny = U.shape
        U += delta[:nx*ny].reshape((nx, ny))
        V += delta[nx*ny:2*nx*ny].reshape((nx, ny))
        P += delta[2*nx*ny:].reshape((nx, ny))
    
    return U, V, P
