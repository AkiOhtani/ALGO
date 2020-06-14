N = int(input())
A = list(map(int, input().split()))

res = 0

for i in range(N - 1):
    boolean = True

    for j in range(i+1, N):
        if A[i] % A[j] == 0:
            boolean = False
            break
    if boolean:
        res += 1
print(res)