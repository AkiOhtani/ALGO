T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())

B = list(map(lambda b: (int(b)-T, int(b)), input().split()))


for bs, be in B:
    boolean = False
    for a in A:
        if bs <= a <= be:
            A.remove(a)
            boolean = True
            break
    if not boolean:
        print('no')
        exit()
print('yes')
    

