from queue import deque
from math import log2

MAX_NUM = 10**16

N = int(input())

primenum = []

for i in range(2, int(log2(N))+1):
    for n in primenum:
        if i % n == 0:
            break
    else:
        primenum.append(i)

kouho_num = set()

for n in primenum:
    for i in range(1, int(log2(MAX_NUM))+1):
        if n**i <= N:
            kouho_num.add(n**i)
        else:
            break

queue = deque([(N, 0, kouho_num)])

res = 0

while queue:
    divnum, countnum, pnum = queue.popleft()
    if divnum == 1:
        res = max(res, countnum)
        continue
    flag = 1
    for num in pnum:
        if divnum % num == 0:
            queue.append((divnum // num, countnum + 1, pnum - set([num])))
            flag = 0
    if divnum > 1 and flag:
        res = max(res, countnum + 1)
print(res)