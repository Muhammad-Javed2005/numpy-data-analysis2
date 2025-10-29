from data_fetch import fetch_data
from simulator import simulate_portfolios
from plotter import plot_comparison



# tickers1 = ['AAPL', 'MSFT', 'GOOG']
# tickers2 = ['BTC-USD', 'DOGE-USD', 'LUNA1-USD']

# tickers1 = ['AAPL', 'MSFT', 'GOOG', 'META']        # Tech Giants – Stable returns
# tickers2 = ['BTC-USD', 'DOGE-USD', 'LUNA1-USD']    # Cryptos – Highly volatile


# tickers1 = ['SPY', 'QQQ', 'DIA', 'VTI']             # Index ETFs – Balanced
# tickers2 = ['SIVBQ', 'BBBYQ', 'MULN', 'LCID']       # Crashed/Penny Stocks


tickers1 = ['KO', 'PEP', 'JNJ', 'PG']
tickers2 = ['NVDA', 'AMD', 'TSLA', 'AMZN']






returns1 = fetch_data(tickers1, '2020-01-01', '2024-12-31')
returns2 = fetch_data(tickers2, '2020-01-01', '2024-12-31')

results1 = simulate_portfolios(returns1)
results2 = simulate_portfolios(returns2)

plot_comparison(results1, results2, tickers1, tickers2)



