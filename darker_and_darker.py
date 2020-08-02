H, W = map(int, input().split())

matrix = []

visited = set()

for i in range(H):
    matrix.append(list(input()))

visited = set()

for i in range(H):
    for j in range(W):
        if matrix[i][j] == '#' and (i, j) not in visited:
            for ud, lr in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if not(0 <= i+ud < H and 0 <= j+lr < W)  or matrix[i+ud][j+lr] == '#':
                    continue
                visited.add((i+ud, j+lr))
                matrix[i+ud][j+lr] = '#'

res = 0

while visited:
    res += 1
    buf = set()
    for i, j in visited:
        if matrix[i][j] == '#' and (i, j) not in buf:
            for ud, lr in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if not(0 <= i+ud < H and 0 <= j+lr < W)  or matrix[i+ud][j+lr] == '#':
                    continue
                buf.add((i+ud, j+lr))
                matrix[i+ud][j+lr] = '#'
    visited = buf
print(res)

