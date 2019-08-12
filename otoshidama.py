N, Y = map(int, input().split())
boolean = False
for i in range(N+1):
    if boolean:
        break
    for j in range(N+1-i):
        if (Y - 10000 * i - 5000 * j) / 1000 == (N - i - j):
            boolean = True
            print(i, j, N - i - j)
            break

if not boolean:
    print(-1, -1, -1)