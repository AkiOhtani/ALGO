def backtrack(res, path):
    if len(path) == N:
        res.append(path)
        return
    for i in range(N):
        if i in path:
            continue
        backtrack(res, path + [i])

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

resA = []
visited = set()
backtrack(resA, [])
resB = []
visited = set()
backtrack(resB, [])

res = 0

for aL in resA:
    for bL in resB:
        res += N // 2 < sum(map(lambda pair: A[pair[0]] > B[pair[1]], zip(aL, bL)))

print(res/(len(resA)*len(resB)))