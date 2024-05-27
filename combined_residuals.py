import numpy as np

def combined_residuals(state, nu, dx, dy, dt, rho):
    nx, ny = (50, 50)
    U, V, P = state[:nx*ny], state[nx*ny:2*nx*ny], state[2*nx*ny:]
    U = U.reshape((nx, ny))
    V = V.reshape((nx, ny))
    P = P.reshape((nx, ny))
    RU, RV, RP = navier_stokes_residuals(U, V, P, nu, dx, dy, dt, rho)
    return np.concatenate([RU.flatten(), RV.flatten(), RP.flatten()])
