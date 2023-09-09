### inital backtest function for 2 tickers w/ start & end date period  ###


import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

class Backtester:
    def __init__(self):
        self.data = {}

    def fetch_data(self, ticker, start_date, end_date):
        try:
            data = yf.download(ticker, start=start_date, end=end_date)
            self.data[ticker] = data
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")

    def backtest(self, ticker1, ticker2, start_date, end_date):
        if ticker1 not in self.data or ticker2 not in self.data:
            print("Data not available for one or more tickers. Please fetch data first.")
            return

        data1 = self.data[ticker1]
        data2 = self.data[ticker2]

        # Perform your backtesting logic here
        # You can access data1 and data2 as Pandas DataFrames

        # Example: Calculate daily returns
        returns1 = data1['Adj Close'].pct_change()
        returns2 = data2['Adj Close'].pct_change()

        # Example: Calculate cumulative returns
        cumulative_returns1 = (1 + returns1).cumprod()
        cumulative_returns2 = (1 + returns2).cumprod()

        # Example: Plot cumulative returns
        plt.figure(figsize=(10, 6))
        plt.plot(data1.index, cumulative_returns1, label=ticker1)
        plt.plot(data2.index, cumulative_returns2, label=ticker2)
        plt.title('Cumulative Returns')
        plt.xlabel('Date')
        plt.ylabel('Cumulative Return')
        plt.legend()
        plt.show()

# Usage example
if __name__ == "__main__":
    backtester = Backtester()
    backtester.fetch_data('AAPL', '2020-01-01', '2023-01-01')
    backtester.fetch_data('MSFT', '2020-01-01', '2023-01-01')
    backtester.backtest('AAPL', 'MSFT', '2020-01-01', '2023-01-01')
