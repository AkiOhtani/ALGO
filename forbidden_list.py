from heapq import heapify, heappush, heappop

X, N = map(int, input().split())

if N == 0:
    print(X)
    exit()

P = list(map(int, input().split()))

nums = []

heapify(nums)

for i in range(0, 102):
    if i not in P:
        heappush(nums, (abs(i - X), i))

print(heappop(nums)[1])