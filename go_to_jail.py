N = int(input())

count = 0

for i in range(N):
    f, s = map(int, input().split())
    if f == s:
        count += 1
        if count == 3:
            print('Yes')
            exit()
    else:
        count = 0
print('No')