# Portfolio Optimization Data Science Project

This data science project aims to perform portfolio optimization using historical stock data. Portfolio optimization is a crucial aspect of investment management, and this project demonstrates the process of constructing an optimal portfolio given a set of assets.

## Problem Formulation

The objective function is to **maximize** the [Sharpe ratio](https://en.wikipedia.org/wiki/Sharpe_ratio) as follows:

```math
\begin{align*}
& \text{Maximize Sharpe Ratio:} \\
& \text{Maximize:} \quad \frac{\sum_{i=1}^{4} w_i \cdot r_i - R_f}{\sqrt{\sum_{i=1}^{4} \sum_{j=1}^{4} (w_i \cdot w_j \cdot \sigma_{ij})}}
\end{align*}
```

_where_
```math
\begin{align*}
& n = 4 \quad \text{(Number of assets)} \\
& w_i \text{'s represent the portfolio weights for assets AAPL, MSFT, GOOGL, TSLA} \\
& r_i \text{'s represent the expected returns for assets AAPL, MSFT, GOOGL, TSLA} \\
& R_f \text{ is the risk-free rate of return} \\
& \sigma_{ij} \text{'s represent the covariance between assets}
\end{align*}
```

_subject to_

```math
\begin{align*}
& \text{Fully Invested Portfolio:} \quad \sum_{i=1}^{4} w_i = 1 \\
& \text{Non-negative Weights:} \quad w_i \geq 0 \quad \text{for } i = 1, 2, 3, 4
\end{align*}
```

## Project Structure

The project is organized into the following directories and files:

- **data**: Contains historical stock and benchmark data in CSV format.
- **notebooks**: Jupyter notebooks for data exploration, analysis, and visualization.
- **scripts**: Python scripts for data collection, preprocessing, portfolio analysis, and optimization.
- **README.md**: This file, providing an overview of the project.
- **requirements.yml**: YAML file listing the Conda packages and their versions required to run the project.

## Data Collection

The `data_collection.py` script fetches historical stock data using the Yahoo Finance API and saves it as `stock_data.csv` in the 'data' directory. You can customize the stock symbol and date range as needed.

## Data Preprocessing

The `data_preprocessing.py` script cleans and preprocesses the stock data, handling missing values, aligning dates, and calculating returns. The preprocessed data is saved as `preprocessed_stock_data.csv` in the 'data' directory.

## Portfolio Analysis

The `portfolio_analysis.py` script calculates various portfolio metrics, such as mean returns, volatility, and correlation coefficients between assets. It also provides an option for Monte Carlo simulations.

## Optimization

The `optimization.py` script implements portfolio optimization techniques to construct an optimal portfolio. You can customize the optimization strategy and constraints according to your preferences. The optimized portfolio weights and metrics are saved as needed.

## How to Run the Project

1. Create a Conda environment using the provided `environment.yml` file:

conda env create -f environment.yml

2. Activate the Conda environment:

conda activate portfolio-optimization


3. Execute the following scripts in the specified order:
- `data_collection.py`
- `data_preprocessing.py`
- `portfolio_analysis.py`
- `optimization.py`

4. Explore and analyze the results in the Jupyter notebooks provided in the notebooks provided.

## Data Sources

- Historical stock data is obtained from Yahoo Finance.
- Benchmark data (e.g., S&P 500) should be provided separately in the 'data' directory as `benchmark_data.csv`.

## Important Notes

- Ensure that you customize the project to match your specific requirements, including stock symbols, date ranges, and optimization techniques.
- This project serves as a demonstration and starting point for portfolio optimization. Advanced techniques and considerations may be required for real-world applications.

## Contributors

- Mariam Walaa

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute to or modify this project as needed. Happy portfolio optimization!

