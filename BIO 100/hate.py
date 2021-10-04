import random

bh=bt=h=t=0
for i in range(50):
    a, b = random.randrange(0, 2), random.randrange(0, 2) # 0 or 1
    if a == b:
        if a == 0: #tails
            bt+=1
        elif b == 1: #heads
            bh+=1
    else:
        h+=1
        t+=1


print(f'{bh}, {bt}, {h}, {t}')
