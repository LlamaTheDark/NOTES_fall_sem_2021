import numpy as np

def test_statistic(x, nh, s, n):
	return (x-nh)/(s/np.sqrt(n))

print(test_statistic(15.583, 15, ))
