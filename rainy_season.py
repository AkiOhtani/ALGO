S = input()
count = 0
res = 0
for c in S:
    if c == 'S':
        count = 0
    else:
        count += 1
        res = max(res, count)
print(res)