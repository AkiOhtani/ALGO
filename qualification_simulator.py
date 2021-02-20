N, A, B = map(int, input().split())
S = input()

for c in S:
    if c == 'b':

        B -= 1
        if B >= 0 and (A+B) >= 0:
            print("Yes")
        else:
            print("No")
    elif c == 'a':
        A -= 1
        if (A+max(0, B)) >= 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")