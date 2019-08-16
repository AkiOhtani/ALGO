from functools import reduce
S = input()

def dfs(res, depth, path, S):
    if len(''.join(path)) == len(S):
        res.append(path)
    for i in range(depth + 1, len(S) + 1):
        dfs(res, i, path + [S[depth:i]], S)

res = []

dfs(res, 0, [], S)

print(sum(int(num) for nums in res for num in nums))
