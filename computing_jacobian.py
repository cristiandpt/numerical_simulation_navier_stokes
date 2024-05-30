import numpy as np
from navier_stokes_residuals import navier_stokes_residuals

def compute_jacobian(U, V, nu, dx, dy, dt, rho, epsilon=1e-3):

    nU = U.size
    nV = V.size
    n = nU #+ nV + nP
    print("La dimension %s" % n)
    J = np.zeros((n, n))
    
    U_flat = U.flatten()
    V_flat = V.flatten()
    
    RU, RV = navier_stokes_residuals(U, V, nu, dx, dy, dt, rho)
    R = np.concatenate([RU.flatten()])
    
    for i in range(n):
        U_pert = U_flat.copy()
        V_pert = V_flat.copy()
        
        if i < nU:
            U_pert[i] += epsilon
        
        U_pert = U_pert.reshape(U.shape)
        V_pert = V_pert.reshape(V.shape)
        
        RU_pert, RV_pert = navier_stokes_residuals(U_pert, V_pert, nu, dx, dy, dt, rho)
        R_pert = np.concatenate([RU_pert.flatten()])
        
        J[:, i] = (R_pert - R) / epsilon
    
    return J
