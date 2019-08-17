from queue import deque
from collections import defaultdict

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

c = []

for i in range(R):
    c.append(list(input()))

visited = set([])
que = deque()
que.append((sy-1, sx-1))
depth_dict = defaultdict(int)
depth_dict[(sy-1, sx-1) ] = 0
minDepth = 2**23 - 1 

while que:
    node = que.popleft()
    if node in visited:
        continue
    else:
        visited.add(node)
        
    for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if node[0] + i < 0 or R - 1 < node[0] + i or node[1] + j < 0 or C - 1 < node[1] + j:
            continue
        elif c[node[0] + i][node[1] + j] == "#":
            continue
        elif node[0] + i == gy - 1 and node[1] + j == gx - 1:
            minDepth = min(minDepth, depth_dict[(node[0], node[1])] + 1)
            break
        else:
            que.append((node[0] + i, node[1] + j))
            depth_dict[(node[0] + i, node[1] + j)] = depth_dict[(node[0], node[1])] + 1 
print(minDepth)