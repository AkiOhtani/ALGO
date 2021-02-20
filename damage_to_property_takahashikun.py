from heapq import heapify, heappush, heappop

H, W = map(int, input().split())

matrix = []

for i in range(H):
    matrix.append(list(input()))
    if 's' in matrix[-1]:
        que = [(-2, i, matrix[-1].index('s'))]

visited = set()
heapify(que)

while que:
    count, row, col = heappop(que)
    if count > 0:
        continue

    if (row, col) in visited:
        continue

    visited.add((row, col))

    if matrix[row][col] == 'g':
        print("YES")
        exit()

    for ud, lr in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if 0 <= row+ud < H and 0 <= col+lr < W:
            heappush(que, (count+1 if matrix[row+ud][col+lr] == '#' else count, row+ud, col+lr))
print("NO")
