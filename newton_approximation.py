import autograd.numpy as np
from autograd import jacobian
from computing_jacobian import compute_jacobian
from navier_stokes_residuals import navier_stokes_residuals
from gauss_seidel_solution import gauss_seidel
from jacobi import jacobi

def newton_raphson(U, V, nu, dx, dy, dt, rho, tol=1e-6, max_iterations=100):
 
    """  for iteration in range(max_iterations):
    
        J = compute_jacobian(U, V, nu, dx, dy, dt, rho)
        
        RU = navier_stokes_residuals(U, V, nu, dx, dy, dt, rho)
        R = np.concatenate([RU.flatten()])
        
        print("iteration %s", iteration)
        print("Norma %s", np.linalg.norm(R, ord=np.inf))
        
        if np.linalg.norm(R, ord=np.inf) < tol:
            print(f"Converged in {iteration} iterations")
            break

        print("J: %s" % RU)
        delta = gauss_seidel(J, -R) """

        
    for k in range(max_iterations):
        RU = navier_stokes_residuals(U, V, nu, dx, dy, dt, rho)
        if np.linalg.norm(RU, ord=np.inf) < tol:
            break
        J = compute_jacobian(U, V, nu, dx, dy, dt, rho)
        print("J: %s" % J)
        delta = gauss_seidel(J, -RU.flatten())
        
        U_flat, V_flat = U.flatten(), V.flatten()
        U_flat += delta[:U.size]
        V_flat += delta[U.size:]
        
        U = U_flat.reshape(U.shape)
        V = V_flat.reshape(V.shape)
       
        nx, ny = U.shape
        U += delta[:nx*ny].reshape((nx, ny))
        #V += delta[nx*ny:2*nx*ny].reshape((nx, ny))
        #P += delta[2*nx*ny:].reshape((nx, ny))
        
    return U # V, P
