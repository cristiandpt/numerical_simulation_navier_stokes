    # It go after of the initialization of the vertion curve
    # line 21
    # Plot the initial approximation
    plt.plot(U_init[:, 0], label='U_initial')
    plt.plot(V_init[:, 0], label='V_initial')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Initial Approximation with Bezier Curve')
    plt.legend()
    plt.grid(True)
    plt.show()

    state = np.concatenate([U.flatten(), V.flatten(), P.flatten()])

    # Calculate Jacobian
    jacobian_func = jacobian(combined_residuals)
    J = jacobian_func(state, nu, dx, dy, dt, rho)
