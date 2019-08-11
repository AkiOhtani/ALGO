def insertionSort(A, N):
    for i in range(1, N):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = v
        print(' '.join(map(lambda x: str(x), A)))
    return A

N = input()

while True:
    try:
        line = raw_input()
        print(line)
        num_list = map(lambda x : int(x), line.strip().split())
        insertionSort(num_list, N)
    except EOFError:
        break