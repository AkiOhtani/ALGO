from sys import maxsize
N, M = map(int, input().split())
bridges = []
for i in range(M):
    a, b = map(int, input().split())
    bridges.append((a, b))

res = 0
end = -maxsize

bridges.sort(key=lambda x: x[1])

for bridge in bridges:
    if end <= bridge[0]:
        res += 1
        end = bridge[1]
print(res)