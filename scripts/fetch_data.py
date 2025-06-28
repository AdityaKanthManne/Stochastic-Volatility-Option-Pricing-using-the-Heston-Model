# fetch_data.py

import yfinance as yf
import pandas as pd
import os

def fetch_options_data(ticker_symbol, save_path, num_expirations=2):
    """
    Fetches options data for a given ticker and saves it as CSV.

    Parameters:
    ticker_symbol : str
        Yahoo Finance ticker symbol (e.g., 'USO' or 'BZ=F')
    save_path : str
        Path to save the CSV file
    num_expirations : int
        Number of expiration dates to fetch
    """
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    ticker = yf.Ticker(ticker_symbol)
    expirations = ticker.options[:num_expirations]

    all_calls = []
    for expiry in expirations:
        try:
            calls = ticker.option_chain(expiry).calls
            calls["expirationDate"] = expiry
            all_calls.append(calls)
        except Exception as e:
            print(f"Failed to fetch options for {expiry}: {e}")

    if all_calls:
        combined_df = pd.concat(all_calls, ignore_index=True)
        combined_df.to_csv(save_path, index=False)
        print(f"Data saved to {save_path}")
    else:
        print("No data retrieved.")

if __name__ == "__main__":
    fetch_options_data("USO", r"C:\Users\adity\OneDrive\Documents\GitHub\Stochastic-Volatility-Option-Pricing-using-the-Heston-Model\data\uso_options_data.csv")
    fetch_options_data("BTC", r"C:\Users\adity\OneDrive\Documents\GitHub\Stochastic-Volatility-Option-Pricing-using-the-Heston-Model\data\brent_options_data.csv")
