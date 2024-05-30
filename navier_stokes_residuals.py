import numpy as np
from navier_stokes_discretized_function import navier_stokes_discretized

def navier_stokes_residuals(U, V, nu, dx, dy, dt, rho):
    
    
    RU = np.zeros_like(U)
  
    f = navier_stokes_discretized() ## The discretized function that models the 2D Navier-Stokes system.
    
    nx, ny = U.shape
    RV = np.ones((ny, ny))

    for i in range(1, nx-1):
        for j in range(1, ny-1):
            result = f(U, V, i, j)
            #print("El current function evaluation: ", result)
            #print("El current U value[i, j]",  U[i, j])
            RU[i, j] = U[i, j] - result
            print("El current RU[%s,%s]= %s" % (i, j, RU[i, j]))
            # Similarly define RV[i, j] and RP[i, j]
            # For simplicity, we'll leave RV and RP as zero here
    
    return RU, RV
