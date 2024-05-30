import numpy as np
from navier_stokes_discretized_function import navier_stokes_discretized
from apply_boundaries_conditions import apply_boundary_conditions

def navier_stokes_residuals(U, V, nu, dx, dy, dt, rho):
    
    RU = np.zeros_like(U)
  
    f = navier_stokes_discretized() ## The discretized function that models the 2D Navier-Stokes system.
    
    apply_boundary_conditions(RU)

    nx, ny = U.shape        # U dimensions

    for i in range(1, nx-1):
        for j in range(1, ny-1):
            result = f(U, V, i, j )   # Apply the discretized function the NS.
            #print("El current function evaluation: ", result)
            RU[i, j] = U[i, j] - result
            #print("El current RU[%s,%s]= %s" % (i, j, RU[i, j]))
            # Similarly define RV[i, j] and RP[i, j]
            # For simplicity, we'll leave RV and RP as zero here
    
    return RU
