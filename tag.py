A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

if V <= W:
    print("NO")
    exit()

diff = max(A, B) - min(A, B)

speed = V - W

if diff <= T * speed:
    print("YES")
else:
    print("NO")
