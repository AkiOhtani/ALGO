N, M = map(int, input().split())
A = set(list(map(int, input().split())))

B = set(map(int, input().split()))

A ^= B

A = list(A)
A.sort()
print(' '.join(map(str, A)))