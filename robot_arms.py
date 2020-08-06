from sys import maxsize
N = int(input())
arms = []
for i in range(N):
    x, l = map(int, input().split())
    arms.append((x-l, x+l))

arms.sort(key=lambda x: x[1])

end = -maxsize

res = 0

for arm in arms:
    if end <= arm[0]:
        res += 1
        end = arm[1]
print(res)
