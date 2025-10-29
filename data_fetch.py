import yfinance as yf

def fetch_data(tickers, start, end):
    # data = yf.download(tickers, start=start, end=end, auto_adjust=True)[tickers]
    data = yf.download(tickers, start=start, end=end, auto_adjust=True)
    return data.pct_change().dropna()
