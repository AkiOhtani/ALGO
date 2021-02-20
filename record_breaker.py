test_count = int(input())
for i in range(test_count):
    N = int(input())
    nums = list(map(int, input().split()))
    backmax = 0
    
    if not nums:
        print("Case #{}: {}".format(i+1, 0))
        break
    
    count = 0
    backmax = -1
    pre = -1
    
    for j in range(len(nums)):
        if backmax == pre and nums[j] < pre:
            count += 1
        if j < len(nums) - 1:
            backmax = max(backmax, nums[j])
        pre = nums[j]
    if backmax < nums[len(nums)-1]:
        count += 1
    print("Case #{}: {}".format(i+1, count))