def bubbleSort(A, N):
    count = 0
    flag = 1
    while flag:
        flag = 0
        for j in range(N - 1, 0, -1):
            if A[j] < A[j - 1]:
                v = A[j]
                A[j] = A[j - 1]
                A[j - 1] = v
                count += 1
                flag = 1
    print(' '.join(map(lambda x: str(x), A)))
    print(count)
    return(A)
N = input()
# for r in range(N):
line = raw_input()
line = line.strip().split()
line = map(lambda x: int(x), line)
bubbleSort(line, N)
