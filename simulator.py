import numpy as np

def simulate_portfolios(returns, num_portfolios=10000):
    mean_returns = returns.mean()
    cov_matrix = returns.cov()

    results = {'returns': [], 'volatility': [], 'sharpe': [], 'weights': []}
    
    for _ in range(num_portfolios):
        weights = np.random.random(len(mean_returns))
        weights /= np.sum(weights)
        
        ret = np.sum(weights * mean_returns) * 252
        vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix * 252, weights)))
        sharpe = ret / vol

        results['returns'].append(ret)
        results['volatility'].append(vol)
        results['sharpe'].append(sharpe)
        results['weights'].append(weights)
    
    return results
