import numpy as np
import moe

def conf_int(x, z, sd, n):
	return (x-((z*sd)/np.sqrt(n)), x+((z*sd)/np.sqrt(n)))

int_1 = conf_int(312, 2.081, 54, 430)
int_2 = conf_int(312, 1.660, 54, 430)

print(moe.moe(2.081, 54, 430))
print(f'96% interval: {int_1}')
print(f'90% interval: {int_2}')

print(f'Range for 96% interval: {int_1[1]-int_1[0]}')
print(f'Range for 90% interval: {int_2[1]-int_2[0]}')

def get_n(z, sd, me):
	return ( (z * sd) / me )**2

print(f'n with desired ME of 10: {get_n(1.660, 56, 10)}')
