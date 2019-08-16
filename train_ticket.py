nums = list(input())
def dfs(res, depth, path, S):
    if depth >= len(S) - 1:
        res.append(path)
        return 
    for char in ['+', '-']:
        dfs(res, depth+1, path+[char], S)

res = []
dfs(res, 0, [], nums)

for comb in res:
    calc = int(nums[0]) 
    string = nums[0]
    for i, func in enumerate(comb):
        if func == '+':
            string += '+' + nums[i+1]
            calc += int(nums[i+1])
        elif func == '-':
            string += '-' + nums[i+1]
            calc -= int(nums[i+1])
    if calc == 7:
        break

print(string+'=7')