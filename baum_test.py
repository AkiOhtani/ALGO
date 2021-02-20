from collections import defaultdict

N, M = map(int, input().split())

adj_list = defaultdict(set)

for i in range(M):
    u, v = map(int, input().split())
    adj_list[u].add(v)
    adj_list[v].add(u)

visited = set()

def dfs(node, parent):
    if node in visited:
        return False
    visited.add(node)

    boolean = True
    for neighbor in adj_list[node]:
        if neighbor == parent:
            continue
        boolean &= dfs(neighbor, node)
    return boolean

res = 0

for node in range(1, N+1):
    if dfs(node, node):
        res += 1
print(res)