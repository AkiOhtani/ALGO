from collections import defaultdict

N, M = map(int, input().split())

adj_list = defaultdict(set)

for i in range(M):
    x, y = map(int, input().split())
    adj_list[x].add(y)
    adj_list[y].add(x)

def judge(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] not in adj_list[nums[i]]:
                return False
    return True

res = 0

for bit in range(0, 1 << N, 1):
    buf = []
    for i in range(N):
        if bit & (1 << i):
            buf.append(i+1)
    #print(buf)
    if judge(buf):
        res = max(res, len(buf))
print(res)