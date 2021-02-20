from queue import deque
H, W = map(int, input().split())
matrix = []
count = 0
for i in range(H):
    matrix.append(list(input()))
    count += matrix[-1].count('.')
que = deque([(0, 0, 1)])

visited = set()

while que:
    row, col, depth = que.popleft()

    if not(0 <= row < H and 0 <= col < W) or matrix[row][col] == '#':
        continue
    
    if (row, col) in visited:
        continue

    visited.add((row, col))
    if (row, col) == (H-1, W-1):
        print(count - depth)
        exit()
    
    for ud, lr in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        que.append((row+ud, col+lr, depth+1))
print(-1)