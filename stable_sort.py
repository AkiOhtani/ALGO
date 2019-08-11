def judegStable(A, B):
    num_dict_input = dict(zip(map(lambda x: str(x), range(1, 10)), [[]] * 9))
    num_dict_output = dict(zip(map(lambda x: str(x), range(1, 10)), [[]] * 9))

    for i in range(0, N):
        num_dict_input[A[i][1]] = num_dict_input[A[i][1]] + [A[i]]
        num_dict_output[B[i][1]] = num_dict_output[B[i][1]] + [B[i]]
    for key, val in num_dict_input.items():
        for i in range(len(val)):
            if val[i] != num_dict_output[key][i]:
                print "Not stable"
                return False
    print "Stable"
    return True


def bubbleSort(A, N):
    for i in range(0, N):
        for j in range(N - 1, i, -1):
            if int(A[j][1]) < int(A[j - 1][1]):
                v = A[j]
                A[j] = A[j - 1]
                A[j - 1] = v
    return A          

def selectionSort(A, N):
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if int(A[j][1]) < int(A[minj][1]):
                minj = j
        v = A[i]
        A[i] = A[minj]
        A[minj] = v
    return A

N = input()
line_ = raw_input()
line = line_.strip().split()
line2 = line_.strip().split()
line3 = line_.strip().split()

output_bubble = bubbleSort(line, N)
print(' '.join(output_bubble))
judegStable(line2, output_bubble)

output_select = selectionSort(line2, N)
print(' ' .join(output_select))
judegStable(line3, output_select)



