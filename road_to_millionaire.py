N = int(input())
A = list(map(int, input().split()))

stock = 1000
num = 0

for i in range(N-1):
    if A[i] < A[i+1]:
        num += stock // A[i]
        stock %= A[i]
    elif A[i] > A[i+1]:
        stock += num * A[i]
        num = 0

print(stock+A[-1]*num) 