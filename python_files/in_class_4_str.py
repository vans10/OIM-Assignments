import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import numpy as np
import pandas as pd
import seaborn as sb
import yfinance as yf
sb.set_theme()

DEFAULT_START = dt.date.isoformat(dt.date.today() - dt.timedelta(days=365))
DEFAULT_END = dt.date.isoformat(dt.date.today())


class Stock:
    def __init__(self, symbol, start=DEFAULT_START, end=DEFAULT_END):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.data = self.get_data()

    def get_data(self):
        """download daily data using yfinance, set a datetimeindex and add returns"""
        df = yf.download(self.symbol, start=self.start, end=self.end, progress=False)

        if df is None or df.empty:
            raise ValueError(f"No data for {self.symbol} from {self.start} to {self.end}")

        if not isinstance(df.index, pd.DatetimeIndex):
            df.index = pd.to_datetime(df.index, errors='coerce')
        df.index.name = 'Date'

        df = self.calc_returns(df)
        self.data = df
        return df

    def calc_returns(self, df):
        """add change and instant_return columns to the data"""
        #change
        if 'Close' not in df.columns:
            raise KeyError("Expected 'Close' column in the downloaded data")

        df['change'] = (df['Close'] - df['Close'].shift(1)) / df['Close'].shift(1)

        # instant_return
        df['instant_return'] = np.log(df['Close']).diff().round(4)

        return df

    def plot_return_dist(self):
        """plot a histogram of the instantaneous returns"""
        if self.data is None or 'instant_return' not in self.data:
            raise ValueError("Run get_data() first to compute returns.")

        plt.figure(figsize=(8, 5))
        plt.hist(self.data['instant_return'].dropna(), bins=50, edgecolor='black')
        plt.title(f"Instantaneous Return Distribution: {self.symbol}")
        plt.xlabel("instantaneous daily return (log)")
        plt.ylabel("frequency")
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.show()

    def plot_performance(self):
        """plot stock performance as percent gain/loss"""
        if self.data is None or 'Close' not in self.data:
            raise ValueError("Run get_data() first to download stock data.")

        close = self.data['Close']
        perf = (close / close.iloc[0]) - 1

        plt.figure(figsize=(8, 5))
        plt.plot(perf.index, perf.values, linewidth=2)
        plt.title(f"Performance of {self.symbol}")
        plt.xlabel("Date")
        plt.ylabel("Percent gain/loss")
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.gca().yaxis.set_major_formatter(tick.PercentFormatter(xmax=1))
        plt.show()


def main():
    test = Stock(symbol='AAPL')  # change ticker if you want
    print(test.data.head())      # access the data attribute
    test.plot_performance()      # plot 1
    test.plot_return_dist()      # plot 2


if __name__ == '__main__':
    main()
