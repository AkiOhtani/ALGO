from functools import lru_cache
N = int(input())
# A * B <= N - 1はいくつありますか？
count = 0
# A ∈ {1, 2, ..., N-1}
for A in range(1, N):
    # B <= (N - 1) // A
    count += (N - 1) // A
print(count)