# Portfolio Optimization Data Science Project

This data science project aims to perform portfolio optimization using historical stock data. Portfolio optimization is a crucial aspect of investment management, and this project demonstrates the process of constructing an optimal portfolio given a set of assets.

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

1. Create a Conda environment using the provided `requirements.yml` file:

conda env create -f requirements.yml

2. Activate the Conda environment:

conda activate portfolio_optimization


3. Execute the following scripts in the specified order:
- `data_collection.py`
- `data_preprocessing.py`
- `portfolio_analysis.py`
- `optimization.py`

4. Explore and analyze the results in the Jupyter notebooks provided in the 'notebooks' directory.

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

