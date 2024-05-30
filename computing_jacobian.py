import numpy as np
from navier_stokes_residuals import navier_stokes_residuals
from apply_boundaries_conditions import apply_boundary_conditions

def compute_jacobian(U, V, nu, dx, dy, dt, rho, epsilon=1e-8):
    nU = U.size
    n = nU
    
    J = np.zeros((n, n))
    
    U_flat = U.flatten()
    V_flat = V.flatten()
    
    RU = navier_stokes_residuals(U, V, nu, dx, dy, dt, rho)
    apply_boundary_conditions(U)
    R = np.concatenate([RU.copy().flatten()])
    
    for i in range(n):
        U_pert = U_flat.copy()
        V_pert = V_flat.copy()
        
        if i < nU:
            U_pert[i] += epsilon + 0.1
        
        U_pert = U_pert.reshape(U.shape)
        V_pert = V_pert.reshape(V.shape)
        
        RU_pert = navier_stokes_residuals(U_pert, V_pert, nu, dx, dy, dt, rho)

        apply_boundary_conditions(U_pert)
        R_pert = np.concatenate([RU_pert.flatten()])

        print("i: %s" % i)
        print("R: %s" % R)
        print("R_pert: %s" % R_pert)
        row, col = J.shape
        print("row: %s, col: %s" % (row, col))

        
        J[:, i] = (R_pert - R) / epsilon
        print("Jacobian: %s" % J)

        print("Jac: %s" % (R_pert - R))
    
    return J

