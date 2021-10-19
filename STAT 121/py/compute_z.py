import numpy as np # for square root, you could also do n**0.5

def compute_z_individual(x, m, sd):
	return (x-m)/sd

def compute_z_sample_mean(x_bar, m, sd, n):
	return compute_z_individual(x_bar, m, sd/np.sqrt(n))

z = compute_z_sample_mean(3, 4.07, 5.2, 36)
print(z)
