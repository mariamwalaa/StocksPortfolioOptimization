# portfolio_analysis.py
import pandas as pd
import numpy as np

def calculate_portfolio_metrics(data):
    """
    Calculate portfolio metrics for a portfolio of assets.

    Args:
        data (pd.DataFrame): DataFrame containing preprocessed data for the portfolio.

    Returns:
        dict: A dictionary containing portfolio metrics.
    """
    # Calculate mean returns and standard deviation for each asset in the portfolio
    returns_columns = [col for col in data.columns if "Returns" in col]
    mean_returns = data[returns_columns].mean()
    std_deviation = data[returns_columns].std()

    # Calculate portfolio weights (e.g., equal weights for simplicity)
    num_assets = len(returns_columns)
    weights = np.array([1 / num_assets] * num_assets)

    # Calculate portfolio expected return and risk
    portfolio_return = np.sum(weights * mean_returns)
    portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(data[returns_columns].cov(), weights)))

    # Create a dictionary to store portfolio metrics
    portfolio_metrics = {
        "Portfolio Return": portfolio_return,
        "Portfolio Risk": portfolio_risk,
        "Mean Returns": mean_returns,
        "Standard Deviation": std_deviation,
        "Weights": weights,
    }

    return portfolio_metrics