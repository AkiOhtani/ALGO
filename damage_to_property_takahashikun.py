from queue import deque

H, W = map(int, input().split())

matrix = []

for i in range(H):
    matrix.append(list(input()))
    if 's' in matrix[-1]:
        que = deque([(i, matrix[-1].index('s'), 2)])

visited = set()

while que:
    row, col, count = que.popleft()
    if count < 0:
        continue

    if (row, col, count) in visited:
        continue

    visited.add((row, col, count))

    if matrix[row][col] == 'g':
        print("YES")
        exit()

    for ud, lr in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if 0 <= row+ud < H and 0 <= col+lr < W:
            que.append((row+ud, col+lr, count-1 if matrix[row+ud][col+lr] == '#' else count))
print("NO")