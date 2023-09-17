# data_preprocessing.py
import pandas as pd
import numpy as np

def preprocess_portfolio_data(data):
    """
    Preprocess historical stock data for a portfolio of assets.

    Args:
        data (pd.DataFrame): DataFrame containing historical data for the portfolio.

    Returns:
        pd.DataFrame: Preprocessed portfolio data.
    """
    # Remove rows with missing values
    data.dropna(inplace=True)

    # Calculate daily returns for each asset in the portfolio
    returns_columns = [col for col in data.columns if "Date" not in col]
    data[returns_columns] = data[returns_columns].pct_change()

    # Calculate log returns for each asset in the portfolio
    log_returns_columns = [f"Log Returns ({col})" for col in returns_columns]
    data[log_returns_columns] = np.log(1 + data[returns_columns])

    # Calculate rolling mean and standard deviation for each asset in the portfolio
    window = 20  # Adjust the window size as needed
    rolling_mean_columns = [f"Rolling Mean ({col})" for col in returns_columns]
    rolling_std_columns = [f"Rolling Std ({col})" for col in returns_columns]
    data[rolling_mean_columns] = data[returns_columns].rolling(window=window).mean()
    data[rolling_std_columns] = data[returns_columns].rolling(window=window).std()

    return data
