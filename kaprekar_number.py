N, K = map(int, input().split())

for i in range(K):
    N = list(str(N))
    g2 = sorted(N)
    g1 = g2[::-1]
    N = int(''.join(g1)) - int(''.join(g2))
print(N)