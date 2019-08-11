K, X = map(int, input().strip().split())
print(' '.join([i for i in range(X-K+1, X+K)]))