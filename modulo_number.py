from math import floor

N = int(input())

num = 998244353

div = floor(N / num)

print(N - num * div)