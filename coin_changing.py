N, M = map(int, input().split())

coins = map(int, input().split())

dp = [0] + [50001 for i in range(N)]

for coin in coins:
    for index in range(N-coin+1):
        dp[index+coin] = min(dp[index+coin], dp[index]+1)
print(dp[N])