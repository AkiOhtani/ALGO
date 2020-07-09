S = input()

res = [[S[0]]]

for c in S[1:]:
    buf = []
    for dp in res[-1]:
        buf.append(dp+c)
        buf.append(dp+'+'+c)
    res.append(buf)
sum_num = 0

for string in res[-1]:
    sum_num += sum(map(int, string.split('+')))
print(sum_num)
