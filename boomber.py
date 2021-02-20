from collections import Counter
H, W, M = map(int, input().split())

maxr, maxc = Counter(), Counter()

mass = set()

for i in range(M):
    h, w = map(int, input().split())
    mass.add((h-1, w-1))
    maxr[h-1]+=1
    maxc[w-1]+=1

res = 0

m = 0 

for r in maxr.keys():
    for c in maxc.keys():
        res = max(res, maxr[r]+maxc[c] - int((r, c) in mass))
print(res)
