import numpy as np

def to_categorical(x, n_col=None):
	# Your code here
	rows = x.shape[0]
	cols = n_col or np.max(x, axis=0) + 1

	one_hot = np.zeros((rows,cols))

	one_hot[np.arange(0, rows), x] = 1

	return one_hot