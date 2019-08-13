from bisect import bisect_left

N, M = map(int, input().split())

P = [0]
for i in range(N):
    P.append(int(input()))

P.sort()

count = 0

for i in range(len(P)):
    for j in range(len(P)):
        for k in range(len(P)):
            num = M - P[i] - P[j] - P[k]
            if num >= 0:
                index = bisect_left(P, num)
                if index == 0 or (index < len(P) and P[index] == num):
                    count = max(count, P[i] + P[j] + P[k] + P[index])
                else:
                    count = max(count, P[i] + P[j] + P[k] + P[index-1])
print(count)