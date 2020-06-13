N, K = map(int, input().split())
A = list(map(int, input().split()))

B = [1 for a in A]

K = min(K, 500)

for k in range(K):
    for i in range(N):
        for j in range(1, A[i]+1):
            if i - j >= 0:
                B[i-j] += 1
            if i + j < N:
                B[i+j] += 1
    A = [b for b in B]
    B = [1 for a in A]

print(' '.join(map(str, A)))