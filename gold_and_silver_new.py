N = int(input())
A = list(map(int, input().split()))
flag = 0
res = []
for i in range(N-1):
    if flag == 0 and  A[i+1] < A[i]:
        flag = 1
        res.append(1)
    elif flag == 1 and A[i] < A[i+1]:
        flag = 0
        res.append(1)
    else:
        res.append(0)
if flag == 1:
    res.append(1)
else:
    res.append(0)
print(' '.join(map(str, res)))