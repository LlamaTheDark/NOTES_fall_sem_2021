import random

bh = bt = fh = ft = 0

for i in range(50):
    first = random.randrange(0, 2)
    second = random.randrange(0, 2)
    if first == 0 and second == 1:
        fh += 1
    elif first == 1 and second == 0:
        ft += 1
    elif first == second:
        if first == 1:
            bh+=1
        else:
            bt+=1

print(f'{bh}, {bt}, {fh}, {ft}')
