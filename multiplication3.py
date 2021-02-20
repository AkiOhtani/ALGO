from decimal import Decimal

A, B = input().split()
A = Decimal(A)
B = Decimal(B)

print(int(A*B))