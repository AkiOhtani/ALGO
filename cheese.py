from queue import deque

H, W, N = map(int, input().split())
matrix = []
    
for i in range(H):
    matrix.append(list(input()))
    for j in range(W):
        if matrix[i][j] == 'S':
            que = deque([(0, i, j, 1)])

visited = set()

while que:
    depth, row, col, vital = que.popleft()
    if (row, col) in visited:
        continue
    visited.add((row, col))
    if str(vital) < matrix[row][col] <= '9': 
        continue
    elif matrix[row][col] == str(vital):
        if matrix[row][col] == str(N):
            print(depth)
            exit() 
        else:
            matrix[row][col] = '.'
            que = deque([(depth, row, col, vital+1)])
            visited = set()
            continue

    for ud, lr in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if not(0 <= row + ud < H and 0 <= col + lr < W and matrix[row+ud][col+lr] != 'X'):
            continue
        que.append((depth+1, row+ud, col+lr, vital))
