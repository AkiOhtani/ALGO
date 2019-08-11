def selectionSort(A, N):
    count = 0
    for i in range(0, N):
        minj = i
        flag = 0
        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j
                flag = 1
        if flag == 1:
            count += 1
        v = A[i]
        A[i] = A[minj]
        A[minj] = v

    return A, count

N = input()

line = raw_input()
line = line.strip().split()
line = map(lambda x: int(x), line)
a = selectionSort(line, N)

print(' '.join(map(lambda x: str(x), a[0])))
print(a[1])