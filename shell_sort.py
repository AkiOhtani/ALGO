def insertionSort(A, N, g):
    for i in range(g, N):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j = j - g
            cnt += 1
        A[j + g] = v

def shellSort(A, N):
    cnt = 0
    m = 
    G[] =
    for i in range(0, m):
        insertionSort(A, N, G[i])

N = input()
A = list([])
for i in range(N):
    A.append(input())

A = shellSort(A, N)

for i in range(N):
    print(A[i])