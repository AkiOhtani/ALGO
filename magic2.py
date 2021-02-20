from queue import deque

A, B, C = map(int, input().split())
K = int(input())

que = deque([(A, B, C, K)])
visited = set()

while que:
    a, b, c, k = que.pop()
    if (a, b, c, k) in visited or k < 0:
        continue
    visited.add((a, b, c, k))
    if k == 0 and a < b < c:
        print('Yes')
        exit()
    que.append((a*2, b, c, k-1))
    que.append((a, b*2, c, k-1))
    que.append((a, b, c*2, k-1))
print('No')