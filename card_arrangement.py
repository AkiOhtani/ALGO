def backtrack(K, string, visited, index):
    if index in visited:
        return
    if K == 0:
        res.add(string + card[index])
        return
    for i in range(N):
        backtrack(K-1, string+card[index], visited|{index}, i)

N = int(input())
K = int(input())
card = []
for i in range(N):
    card.append(input())
res = set()

visited = set()

for i in range(N):
    backtrack(K-1, '', visited, i)
print(len(res))