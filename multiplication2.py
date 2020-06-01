N = int(input())
A = map(int, input().split())

if 0 in A:
    print(0)
    exit(0)
mul = 1
for a in A:
    mul *= a
    if mul > 1e18:
        print('-1')
        exit(0)
print(mul)