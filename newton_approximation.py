import numpy as np
from computing_jacobian import compute_jacobian
from navier_stokes_residuals import navier_stokes_residuals
from gauss_seidel_solution import gauss_seidel

def newton_raphson(U, V, P, nu, dx, dy, dt, rho, tol=1e-6, max_iterations=1):

    for iteration in range(max_iterations):
    
        J = compute_jacobian(U, V, nu, dx, dy, dt, rho)
        print(J)
        RU, RV = navier_stokes_residuals(U, V, nu, dx, dy, dt, rho)
        R = np.concatenate([RU.flatten()])
        
        print("iteration %s", iteration)
        print("Norma %s", np.linalg.norm(R, ord=np.inf))
        
        if np.linalg.norm(R, ord=np.inf) < tol:
            print(f"Converged in {iteration} iterations")
            break

        delta = gauss_seidel(J, -R)

       
        nx, ny = U.shape
        U += delta[:nx*ny].reshape((nx, ny))
        #V += delta[nx*ny:2*nx*ny].reshape((nx, ny))
        #P += delta[2*nx*ny:].reshape((nx, ny))
        
    return U, # V, P
