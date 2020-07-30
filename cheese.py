from queue import deque

H, W, N = map(int, input().split())
matrix = []
    
for i in range(H):
    matrix.append(list(input()))
    for j in range(W):
        if matrix[i][j] == 'S':
            que = deque([(0, i, j, 1, set())])
    
while que:
    depth, row, col, vital, visited = que.popleft()
    if str(vital) < matrix[row][col] and '0' < matrix[row][col] <= '9': 
        continue
    
    if '.' < matrix[row][col] <= str(vital):
        if (row, col) not in visited:
            vital += 1
            visited.add((row, col))
    if matrix[row][col] == str(N):
        print(depth)
        exit() 

    for ud, lr in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if not(0 <= row + ud < H and 0 <= col + lr < W and matrix[row+ud][col+lr] != 'X'):
            continue
        que.append((depth+1, row+ud, col+lr, vital, visited))
            