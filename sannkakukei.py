from bisect import bisect_left

N = int(input())
a = list(map(int, input().split()))

a.sort()

ed = N-1

res = 0

while 1 < ed:
    i = bisect_left(a[:ed-1], a[ed]-a[ed-1]) + 1
    if i  < ed - 1:
        res = max(res, a[i] + a[ed-1] + a[ed])
    ed -= 1
print(res)