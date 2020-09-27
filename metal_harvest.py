from math import ceil
from sys import maxsize

T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    start = 0
    count = 0
    for j in range(N):
        s, e = map(int, input().split())
        start = max(start, s)
        if start < e:
            count += ceil((e-start)/K)
        start = max(e, start + K*ceil((e-start)/K))
    print("Case #{}: {}".format(str(i+1), str(count)))