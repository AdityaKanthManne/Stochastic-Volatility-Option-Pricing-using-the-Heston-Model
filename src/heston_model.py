import numpy as np

def simulate_heston_paths(S0, v0, r, kappa, theta, sigma, rho, T, N, M):
    """
    Simulates M price paths under the Heston model using the Euler-Maruyama scheme.

    Parameters:
    S0     : initial asset price
    v0     : initial variance
    r      : risk-free interest rate
    kappa  : rate of mean reversion
    theta  : long-term variance
    sigma  : volatility of variance
    rho    : correlation between asset and volatility
    T      : time to maturity
    N      : number of time steps
    M      : number of simulations

    Returns:
    S_paths: simulated asset price paths (M x N+1)
    v_paths: simulated variance paths (M x N+1)
    """
    dt = T / N
    S_paths = np.zeros((M, N + 1))
    v_paths = np.zeros((M, N + 1))

    S_paths[:, 0] = S0
    v_paths[:, 0] = v0

    for t in range(1, N + 1):
        z1 = np.random.normal(size=M)
        z2 = np.random.normal(size=M)
        W1 = z1
        W2 = rho * z1 + np.sqrt(1 - rho**2) * z2

        vt = np.maximum(v_paths[:, t - 1], 0)
        v_paths[:, t] = (
            vt + kappa * (theta - vt) * dt + sigma * np.sqrt(vt * dt) * W2
        )
        v_paths[:, t] = np.maximum(v_paths[:, t], 0)

        S_paths[:, t] = (
            S_paths[:, t - 1] * np.exp((r - 0.5 * vt) * dt + np.sqrt(vt * dt) * W1)
        )

    return S_paths, v_paths


def heston_option_price(S0, K, T, r, v0, kappa, theta, sigma, rho, option_type="call", N=252, M=10000):
    """
    Monte Carlo pricing of European options under the Heston model.

    Parameters:
    All same as simulate_heston_paths
    option_type : 'call' or 'put'

    Returns:
    Estimated option price
    """
    S_paths, _ = simulate_heston_paths(S0, v0, r, kappa, theta, sigma, rho, T, N, M)
    ST = S_paths[:, -1]

    if option_type == "call":
        payoff = np.maximum(ST - K, 0)
    elif option_type == "put":
        payoff = np.maximum(K - ST, 0)
    else:
        raise ValueError("Invalid option_type. Choose 'call' or 'put'.")

    return np.exp(-r * T) * np.mean(payoff)
