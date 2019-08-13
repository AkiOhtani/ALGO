from bisect import bisect_left

N, M = map(int, input().split())

P = [0]
for i in range(N):
    P.append(int(input()))

P.sort()

combP = set()
for numi in P:
    for numj in P:
        if (numi + numj) not in combP:
            combP.add(numi + numj)

combP = sorted(list(combP))

count = []

for numi in combP:
    num = M - numi
    if num >= 0:
        index = bisect_left(combP, num)
        if index == 0 or (index < len(P) and P[index] == num):
            count.append(numi + combP[index])
        else:
            count.append(numi + combP[index-1])

print(max(count))