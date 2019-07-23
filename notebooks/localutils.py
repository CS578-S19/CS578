# =============================================================================
# Utility functions for CS578 - Spring 2019
# =============================================================================


import numpy as np
import pandas as pd


# =============================================================================
# Entropy and Information Gain
# =============================================================================

def entropy(prob):
    """Compute and return entropy for a discrete prob distribution."""
    e = 0
    for p in prob:
        if p > 0:
            e += -1*(p*np.log2(p))
    return e

def entropy_counts(counts):
    """Compute and return entropy for a discrete count."""
    c = np.asarray(counts)
    p = c/np.sum(c)
    return entropy(p)

def expected_split_entropy(leaves):
    """Compute expected entropy of the given split counts."""
    leaves = np.asarray(leaves)
    entropies = np.asarray(list(map(entropy_counts, leaves)))
    sums = np.sum(leaves, axis=1)
    probs = sums/np.sum(sums)
    return np.sum(probs*entropies)

def information_gain(root, leaves):
    """Compute information gain given the counts at the root and the leaves."""
    e_root = entropy_counts(root)
    e_leaves = expected_split_entropy(leaves)
    return e_root - e_leaves

def mutual_info(counts):
    """Mutual information between a discrete X and a discrete Y.
    
    Argument
    counts -- A list of lists.
    """
    counts = np.asarray(counts)
    jp = counts/counts.sum()
    px = np.sum(jp, axis=1)
    py = np.sum(jp, axis=0)
    mi = 0
    for i in range(len(px)):
        for j in range(len(py)):
            mi += jp[i, j]*np.log2(jp[i, j]/(px[i]*py[j]))
    return mi

def chi2(counts):
    """Chi2 between a discrete X and a discrete Y.
    
    Argument
    counts -- A list of lists.
    """
    counts = np.asarray(counts)
    jp = counts/counts.sum()
    px = np.sum(jp, axis=1)
    py = np.sum(jp, axis=0)
    m = counts.sum()
    cs = 0
    for i in range(len(px)):
        for j in range(len(py)):
            cs += ((counts[i, j] - m*px[i]*py[j])**2) / (m*px[i]*py[j]) 
    return cs

# =============================================================================
# Load Simulated Data from Hugin
# =============================================================================

def load_hugin_dataset(filename, target_feature):
    """Load a dataset simulated from a Hugin file."""
    df=pd.read_csv(filename)
    y=np.asarray(df[target_feature].values, dtype=str)
    X=df.loc[:, df.columns != target_feature].values
    feature_names = df.loc[:, df.columns != target_feature].columns.values
    return X, y, feature_names