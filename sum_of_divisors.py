N = int(input())

res = 0

for i in range(1, N+1):
    j = N // i
    res += j*(j+1)*i//2
print(res)