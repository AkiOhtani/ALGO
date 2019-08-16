def dfs(res, depth, path, P, C, G):
    if sum((index + 1) * 100 for index in path) >= G:
        res[0] = min(res[0], len(path))
        return
    elif depth == len(C):
        return
    for j in range(P[depth] + 1):
        if j == P[depth]:
            dfs(res, depth + 1, path + [depth] * j, P, C, G - C[depth])
        else:
            dfs(res, depth + 1, path + [depth] * j, P, C, G)

D, G = map(int, input().split())
P, C = [], []
for i in range(D):
    p, c = map(int, input().split())
    P.append(p)
    C.append(c)

res = [sum(P)]
dfs(res, 0, [], P, C, G)
print(res[0])
