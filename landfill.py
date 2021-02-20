N = 10

matrix = []

for i in range(N):
    matrix.append(list(input()))

def dfs(row, col):
    if row < 0 or col < 0 or N <= row or N <= col or matrix[row][col] == 'x':
        return False
    elif (row, col) in visited:
        return False
    visited.add((row, col))

    for lr, ud in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        dfs(row+lr, col+ud)
    return True

def judge():
    res = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == "o" and dfs(i, j):
                res += 1
    return res == 1

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'x':
            matrix[i][j] = 'o'
            visited = set()
            if judge():
                print("YES")
                exit()
            matrix[i][j] = 'x'
if judge():
    print("YES")
else:
    print("NO")