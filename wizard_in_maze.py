from queue import deque

H, W = map(int, input().split())
Si, Sj = map(int, input().split())
Gi, Gj = map(int, input().split())
matrix = []
for i in range(H):
    matrix.append(list(input()))

que = deque([(0, Si-1, Sj-1)])
visited = set()

while que:
    count, r, c = que.popleft()
    if not(0 <= r < H and 0 <= c < W):
        continue
    if (r, c) in visited:
        continue
    elif matrix[r][c] == '#':
        continue
    elif (r, c) == (Gi-1, Gj-1):
        print(count)
        exit()
    visited.add((r, c))
    for td, lr in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        que.appendleft((count, r+td, c+lr))
    for ud in range(-2, 3):
        for lr in range(-2, 3):
            que.append((count+1, r+ud, c+lr))
print('-1')
