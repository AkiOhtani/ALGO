import sys
MAX_INT = sys.maxsize
test_count = int(input())
dp = [[0]*4]

for i in range(test_count):
    N = int(input())
    nums = list(map(int, input().split()))

    for j in range(1, len(nums)):
        buf = []

        if nums[j-1] < nums[j]:
            for k in range(4):
                lower = min(dp[-1][:k+1]) if dp[-1][:k+1] else MAX_INT
                upper =  min(dp[-1][k+1:]) if dp[-1][k+1:] else MAX_INT
                buf.append(min(upper, 1 + lower))
        elif nums[j-1] == nums[j]:
            for k in range(4):
                lower = min(dp[-1][:k]) if dp[-1][:k] else MAX_INT
                upper =  min(dp[-1][k+1:]) if dp[-1][k+1:] else MAX_INT
                buf.append(min(min(dp[-1][k], 1 + lower), 1 + upper))
        else:
            for k in range(4):
                lower = min(dp[-1][:k+1]) if dp[-1][:k+1] else MAX_INT
                upper =  min(dp[-1][k+1:]) if dp[-1][k+1:] else MAX_INT
                buf.append(min(1+upper, lower))
        dp.append(buf)
    print("Case #{}: {}".format(i+1, min(dp[-1])))