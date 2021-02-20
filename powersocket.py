from math import ceil
A, B = map(int, input().split())
if B == 1:
    print(0)
else:
    print(int(ceil((B-1)/(A-1))))