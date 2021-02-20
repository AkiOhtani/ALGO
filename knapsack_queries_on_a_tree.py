def knapsack(v, l, W, V):
    res = [[0] for i in range(v+1)]
    cos = [[l] for i in range(v+1)]

    for i in range(v):
        for j in range(len(cos[i])):
            if cos[i][j] - W[i] >= 0:
                res[i+1].append(res[i][j] + V[i])
                cos[i+1].append(cos[i][j] - W[i])
    return max(res[-1])

N = int(input())
V, W = [], []

for i in range(N):
    v, w = map(int, input().split())
    V.append(v)
    W.append(w)

Q = int(input())

V2, L = [], []

for i in range(Q):
    vv, l = map(int, input().split())
    V2.append(vv)
    L.append(l)

for vv, l in zip(V2, L):
    print(knapsack(vv, l, W, V))