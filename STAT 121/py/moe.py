import numpy as np

def moe(z, sd, n):
	return z*(sd/np.sqrt(n))

def calc_conf(x, z, sd, n):
	return (x-moe(z, sd, n), x+moe(z, sd, n))

z_ = 1.645
sd_ = 18
x_ = 195


# print(calc_conf(195, 1.96, 18, 100))


# print(f'required n = {((sd_*z_)/6.8)**2}')

print(calc_conf(1.811868, 1.96, 3.3, 1648))

print(moe(1.96, 3.3, 1648))
