from math import ceil, floor

h1, m1, h2, m2, k = map(int, input().split())

diff = (h2-h1)*60 + (m2-m1) 

print('%d' % max(0, diff-k))