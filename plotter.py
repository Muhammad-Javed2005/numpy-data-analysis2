import matplotlib.pyplot as plt

def plot_comparison(res1, res2, tickers1, tickers2):
    fig, axs = plt.subplots(1, 2, figsize=(15, 6))

    axs[0].scatter(res1['volatility'], res1['returns'], c=res1['sharpe'], cmap='viridis', alpha=0.6)
    axs[0].set_title(f"Portfolio: {', '.join(tickers1)}")
    axs[0].set_xlabel("Volatility")
    axs[0].set_ylabel("Expected Return")
    axs[0].grid(True)

    axs[1].scatter(res2['volatility'], res2['returns'], c=res2['sharpe'], cmap='plasma', alpha=0.6)
    axs[1].set_title(f"Portfolio: {', '.join(tickers2)}")
    axs[1].set_xlabel("Volatility")
    axs[1].set_ylabel("Expected Return")
    axs[1].grid(True)

    plt.suptitle("Comparison of Two Portfolios", fontsize=16)
    plt.tight_layout()
    plt.show()
