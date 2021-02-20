from queue import deque
from copy import deepcopy

def copyAndAlter(origin, p, a):
    matrix_ = deepcopy(origin)
    buf = matrix_[p].pop()
    matrix_[a].append(buf)
    return matrix_

while 1:
    N, M = map(int, input().split())
    if N == M == 0:
        break

    matrix = []
    
    for i in range(3):
        matrix.append(list(input().split()[1:]))

    res = M + 1

    que = deque([(0, matrix)])
    visited = set()

    while que:
        depth, matrix = que.popleft()
        if M < depth:
            continue

        if repr(matrix) in visited:
            continue

        visited.add(repr(matrix))

        if not matrix[1]:
            if not matrix[0] or not matrix[2]:
                res = min(res, depth)
                break

        for p, a in ((0, 1), (1, 0), (1, 2), (2, 1)):
            if not matrix[p]:
                continue
            if matrix[a] and matrix[p][-1] < matrix[a][-1]:
                continue
            que.append((depth+1, copyAndAlter(matrix, p, a)))
    print(-1 if res == M + 1 else res)
