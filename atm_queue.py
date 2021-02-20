from heapq import heapify, heappush, heappop, nsmallest
from math import ceil

T = int(input())
for i in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    heapq = []
    heapify(heapq)

    for j in range(N):
        heappush(heapq, (ceil(A[j]/X), j+1))
    print("Case #{}: {}".format(str(i+1), ' '.join([str(pair[1]) for pair in nsmallest(N, heapq)])))