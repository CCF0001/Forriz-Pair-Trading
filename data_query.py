# %%
pip install yfinance pandas

# %%
import yfinance as yf
import pandas as pd

# %%
source_file = pd.read_csv("HSI_30May25.csv")
tickers_list = source_file['Stock Code'].tolist()

# %%
def download_stock_price(tickers):
    for ticker in tickers:
        ticker = ticker.strip()
        stock = yf.Ticker(ticker)
        price = stock.history(start="2020-01-01", end=None)
        price.to_csv(f"data/{ticker}.csv")

download_stock_price(tickers_list)


