import numpy as np
from navier_stokes_residuals import navier_stokes_residuals
from apply_boundaries_conditions import apply_boundary_conditions

def compute_jacobian(U, V, nu, dx, dy, dt, rho, epsilon=1e-8):
    nU = U.size
    nV = V.size
    n = nU
    
    J = np.zeros((n, n))
    
    U_flat = U.flatten()
    V_flat = V.flatten()
    
    RU = navier_stokes_residuals(U, V, nu, dx, dy, dt, rho)
    apply_boundary_conditions(U)  # Aplica condiciones de frontera a U y V
    R = np.concatenate([RU.flatten()])
    
    for i in range(n):
        U_pert = U_flat.copy()
        V_pert = V_flat.copy()
        
        if i < nU:
            U_pert[i] += epsilon  # Solo suma epsilon, no epsilon + 1
        else:
            V_pert[i - nU] += epsilon
        
        U_pert = U_pert.reshape(U.shape)
        V_pert = V_pert.reshape(V.shape)
        
        apply_boundary_conditions(U_pert)  # Aplica condiciones de frontera a U_pert y V_pert
        
        RU_pert = navier_stokes_residuals(U_pert, V_pert, nu, dx, dy, dt, rho)
        R_pert = np.concatenate([RU_pert.flatten()])

        print(f"i: {i}")
        print(f"R: {R}")
        print(f"R_pert: {R_pert}")
        
        J[:, i] = (R_pert - R) / epsilon

        print(f"Jac: {J[:, i]}")
    
    return J

# Ejemplo de uso:
nx, ny = 50, 5  # Tamaño de la malla
nu = 0.1  # Viscosidad cinemática
dx, dy = 1.0 / nx, 1.0 / ny  # Espaciamiento de la malla
dt = 0.01  # Paso de tiempo
rho = 1.0  # Densidad

# Condiciones iniciales
U = np.zeros((nx, ny))
V = np.zeros((nx, ny))
U[:, 0] = 1  # Primera columna llena de unos como condición de frontera

# Calcular el Jacobiano
J = compute_jacobian(U, V, nu, dx, dy, dt, rho)
