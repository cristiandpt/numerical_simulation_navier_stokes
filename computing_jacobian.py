import numpy as np
from navier_stokes_residuals import navier_stokes_residuals

def compute_jacobian(U, V, P, nu, dx, dy, dt, rho, epsilon=1e-8):

    nU = U.size
    nV = V.size
    nP = P.size
    n = nU + nV + nP
    
    J = np.zeros((n, n))
    
    U_flat = U.flatten()
    V_flat = V.flatten()
    P_flat = P.flatten()
    
    RU, RV, RP = navier_stokes_residuals(U, V, P, nu, dx, dy, dt, rho)
    R = np.concatenate([RU.flatten(), RV.flatten(), RP.flatten()])
    
    for i in range(n):
        U_pert = U_flat.copy()
        V_pert = V_flat.copy()
        P_pert = P_flat.copy()
        
        if i < nU:
            U_pert[i] += epsilon
        elif i < nU + nV:
            V_pert[i - nU] += epsilon
        else:
            P_pert[i - nU - nV] += epsilon
        
        U_pert = U_pert.reshape(U.shape)
        V_pert = V_pert.reshape(V.shape)
        P_pert = P_pert.reshape(P.shape)
        
        RU_pert, RV_pert, RP_pert = navier_stokes_residuals(U_pert, V_pert, P_pert, nu, dx, dy, dt, rho)
        R_pert = np.concatenate([RU_pert.flatten(), RV_pert.flatten(), RP_pert.flatten()])
        
        J[:, i] = (R_pert - R) / epsilon
    
    return J
