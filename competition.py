from math import ceil
X, Y, Z = map(int, input().split())
Y /= X * 1.0

Z = ceil(Z * Y - 1.0)

print(Z)