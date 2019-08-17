from copy import deepcopy
from sys import setrecursionlimit
setrecursionlimit(10000*10000)

def dfs(res, rowidx, colidx, path, C, H, W):
    C[rowidx][colidx] = "X"

    if res[0]:
        return
    elif path == "g":
        res[0] = True
        return
    elif path == "#" or path == "X":
        return
    else:
        for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if rowidx + i < 0 or H - 1 < rowidx + i or colidx + j < 0 or W - 1 < colidx + j:
                continue
            dfs(res, rowidx + i, colidx + j, C[rowidx + i][colidx + j], C, H, W) 

H, W = map(int, input().split())

C = []
si, sj = [], []

for i in range(H):
    C.append(list(input()))

    if "s" in C[-1]:
        for j in range(W):
            if C[i][j] == "s":
                si.append(i)
                sj.append(j)

res = [False]

for i, j in zip(si, sj):
    if res[0]:
        break
    buf = deepcopy(C)
    dfs(res, i, j, "s", buf, H, W)

if res[0]:
    print("Yes")
else:
    print("No")