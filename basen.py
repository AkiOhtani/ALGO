from math import floor, ceil

X = input()
M = int(input())

d = int(max(X))

if len(X) == 1:
    if int(X) <= M:
        print(1)
    else:
        print(0)
    exit()

st = d
ed = M + 1

while st + 1 < ed:
    mid = (st + ed) // 2
    sum = 0
    for c in X:
        if sum > M // mid:
            sum = M + 1
            break
        else:
            sum = sum * mid + int(c)
    if sum <= M:
        st = mid
    else:
        ed = mid
print(st-d)