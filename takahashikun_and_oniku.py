N = int(input())
t = []
for i in range(N):
    t.append(int(input()))
dp = [[[t[0]], [-t[0]]]]

for num in t[1:]:
    buf = []
    for l in dp[-1]:
        buf.append(l+[num])
        buf.append(l+[-num])
    dp.append(buf)

print(min(max(-sum(filter(lambda x: x < 0, l)), sum(filter(lambda x: x > 0, l))) for l in dp[-1]))