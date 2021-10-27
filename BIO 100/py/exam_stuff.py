import numpy as np

n1 = 152*2
n2 = 160*2

C_n1 = (27*2) + 97
T_n1 = (28*2) + 97

C_n2 = (85*2) + 47
T_n2 = (28*2) + 47

print(f'C_n1: {C_n1/n1} \nT_n1: {T_n1/n1} \nC_n2: {C_n2/n2} \nT_n2: {T_n2/n2}',end='\n\n\n')

Q_n1 = (5*2) + 33
R_n1 = (114*2) + 33

Q_n2 = (21*2) + 69
R_n2 = (70*2) + 69

print(f'Q_n1: {Q_n1/n1} \nR_n1: {R_n1/n1} \nQ_n2: {Q_n2/n2} \nR_n2: {R_n2/n2}',end='\n\n\n')


print(f'{2*.86*.14*152}')
