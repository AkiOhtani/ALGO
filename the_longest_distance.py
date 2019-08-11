import math
def squareEuclidDistance(x1, x2, y1, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

N = int(input())
X, Y = [], []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

res = [0 for i in range(N*(N-1)//2)]
for i in range(N):
    for j in range(i+1, N):
        distance = squareEuclidDistance(X[i], X[j], Y[i], Y[j])
        if res[i] < distance:
            res[i] = distance
print(max(res))