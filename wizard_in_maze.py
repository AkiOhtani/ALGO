from heapq import heapify, heappop, heappush

H, W = map(int, input().split())
Si, Sj = map(int, input().split())
Gi, Gj = map(int, input().split())
matrix = []
for i in range(H):
    matrix.append(list(input()))

que = [(0, 0, Si-1, Sj-1)]
heapify(que)
visited = set()

while que:
    count, priority, r, c = heappop(que)
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
        heappush(que, (count, priority+1, r+td, c+lr))
    for ud in range(-2, 3):
        for lr in range(-2, 3):
            heappush(que, (count+1, priority+1, r+ud, c+lr))
print('-1')
