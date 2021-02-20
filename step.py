N = int(input())
A = list(map(int, input().split()))

maxt = 0
res = 0
for i in range(N):
    maxt = max(maxt, A[i])
    res += maxt - A[i]
print(res)