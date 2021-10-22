import numpy as np

def me(conf, sd, n):
	return (conf*sd)/np.sqrt(n)

print(me(2.054, 54, 430))

print((2.054 * 54)/np.sqrt(430))
