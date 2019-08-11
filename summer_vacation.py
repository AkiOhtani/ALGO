def dfs(res, depth, path, A, B, time, M):
    res.append(path)
    for i in range(depth, len(A)):
        if time + A[i] <= M:
            dfs(res, i+1, path + [B[i]], A, B, time + 1, M)

N, M = map(int, input().split())

A, B = [], []
res = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

C, D = [], []
for c, d in sorted(zip(A,B), key=lambda x: x[0], reverse=True):
    C.append(c)
    D.append(d)
    
del A, B
    
dfs(res, 0, [], C, D, 0, M)
print(sum(sorted(res, key=lambda x: sum(x))[-1])) if res else print(0)