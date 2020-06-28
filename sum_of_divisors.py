from math import sqrt

N = int(input())

#A = [i for i in range(1, N+1)]

res = sum(range(1, N+1))

for i in range(2, N+1):
    for j in range(i, int(sqrt(i))+1):
        if i % j == 0:
            #A[j-1] += i
            res += i
print(res)