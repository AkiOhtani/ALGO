T = int(input())
for i in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    diff = A[1] - A[0]
    count = 2
    maxcount = 2
    for j in range(2, N):
        if A[j] - A[j-1] == diff:
            count += 1
            maxcount = max(maxcount, count)
        else:
            diff = A[j] - A[j-1]
            count = 2
    print("Case #{}: {}".format(i, maxcount))