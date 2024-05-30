def apply_boundary_conditions(U):
    """
    Apply boundary conditions to the velocity and pressure fields.
    For this example, the first column of U is set to 1, and other boundaries are set to 0.
    """
    nx, ny = U.shape
    
    # Set the first column of U to 1
    
    
    # Set other boundaries to 0
    U[:, -1] = 0
    U[0, :] = 0
    U[-1, :] = 0
    U[:, 0] = 1
    U[-1, -1] = 0.01
    