S = 1000 - int(input())

res = 0
for coin in (500, 100, 50, 10, 5, 1):
    res += S // coin
    S %= coin
print(res)