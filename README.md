# Stochastic Volatility Option Pricing using the Heston Model

This project explores how stochastic volatility models, particularly the Heston model, enhance option pricing accuracy and hedging performance under volatile market conditions. Unlike the Black-Scholes model, which assumes constant volatility, the Heston model allows volatility itself to evolve stochastically—capturing real-world phenomena like volatility clustering and fat tails.

## Context

In an increasingly unstable global environment, oil markets are highly sensitive to geopolitical shocks, supply disruptions, and policy shifts. Traditional models like Black-Scholes fall short in capturing market behavior during such events due to their constant volatility assumption.

This project uses the Heston model to simulate more realistic option pricing on oil-based assets like:
- USO ETF (proxy for U.S. oil exposure)
- Brent Crude Futures (proxy for Iranian oil exposure)

## Objectives

- Implement the Heston stochastic volatility model via Monte Carlo simulation
- Simulate asset paths and option prices under stochastic volatility
- Compare pricing and hedging performance against the Black-Scholes model
- Analyze the model’s behavior under extreme market scenarios

## Project Structure

```
stochastic-volatility-pricing/
├── data/
│   ├── uso_options_data.csv
│   └── brent_options_data.csv
├── notebooks/
│   └── Heston_Simulation_Analysis.ipynb
├── src/
│   └── heston_model.py
├── scripts/
│   └── fetch_data.py
├── plots/
├── README.md
└── requirements.txt
```

## Key Concepts

- Stochastic Volatility: Models volatility as a separate random process
- Mean-Reversion: Volatility tends to revert to a long-term average
- Vol-of-Vol: Captures how uncertain volatility itself is
- Correlation: Between asset returns and volatility innovations

## Technologies Used

- Python 3
- NumPy, SciPy
- Matplotlib, Seaborn
- Jupyter Notebook
- yFinance (data retrieval)

## Model Parameters

- Initial asset price (S₀)
- Strike price (K)
- Time to maturity (T)
- Risk-free rate (r)
- Initial variance (v₀)
- Long-run variance (θ)
- Mean reversion rate (κ)
- Volatility of volatility (σ)
- Correlation (ρ)

## Output

- Simulated paths of asset prices and volatility
- Heston-based option prices vs. Black-Scholes prices
- Absolute and percentage pricing errors
- Visual comparison of hedging performance

## Future Work

- Calibrate Heston parameters using real market data
- Compare with SABR or rough volatility models
- Apply to FX or equity index options under geopolitical risk

## Author

Aditya Kanth Manne  

