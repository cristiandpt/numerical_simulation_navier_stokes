import numpy as np
from navier_stokes_discretized_function import navier_stokes_discretized

def navier_stokes_residuals(U, V, P, nu, dx, dy, dt, rho):
    
    
    RU = np.zeros_like(U)
    RV = np.zeros_like(V)
    RP = np.zeros_like(P)
  
    f = navier_stokes_discretized() ## The discretized function that models the 2D Navier-Stokes system.
    
    nx, ny = U.shape
    for i in range(1, nx-1):
        for j in range(1, ny-1):
            RU[i, j] = U[i, j] - f(U, V, i, j)
            # Similarly define RV[i, j] and RP[i, j]
            # For simplicity, we'll leave RV and RP as zero here
    
    return RU, RV, RP
