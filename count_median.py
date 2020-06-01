N = int(input())

A, B = [], []

a, b = None, None

sum = [0 for i in range(N)]

for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A.sort()
B.sort()

if N % 2 == 1:
    print(B[N//2] - A[N//2] + 1)
else:
    print(B[N//2-1]+B[N//2] - A[N//2-1]-A[N//2]+1)