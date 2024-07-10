import numpy as np

def ksaai(X, Y, ties=True):
    np.random.seed(69)
    n = len(X)
    
    order = np.argsort(X)
    ranks = np.argsort(Y[order])
    diff_ranks = np.abs(np.diff(ranks))
    
    if ties:
        counts = np.bincount(ranks)
        ranks += np.random.uniform(0, counts[ranks] - 1)
        l = np.bincount(ranks).astype(float)
        return 1 - n * np.sum(diff_ranks) / (2 * np.sum(l * (n - l)))
    else:
        return 1 - 3 * np.sum(diff_ranks) / (n**2 - 1)