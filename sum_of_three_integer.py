K, S = map(int, input().split())

res = 0

for X in range(min(S, K), -1, -1):
    for Y in range(min(K, S - X), -1, -1):
        if 0 <= S - X - Y <= K:
            res += 1
print(res)