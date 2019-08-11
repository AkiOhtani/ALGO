import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
A = list(map(int, input().strip().split()))
min_num = min(A)
for i in range(M):
    B, num = map(int, input().strip().split())
    if num <= min_num:
        continue
    else:
        min_num = num
    for j in range(B):
        index = A.index(min(map(lambda x: x - num, A))+num)
        if A[index] < num:
            A[index] = num
        else:
            break
print(sum(A))