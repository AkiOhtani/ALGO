T = int(input())

from collections import Counter, deque

comp = Counter()

for i in range(T):
    R, G, B = map(int, input().split())
    if ' '.join(map(str, sorted([R, G, B]))) in comp:
        print(comp[' '.join(map(str, sorted([R, G, B])))])
        continue
    N = R + G + B
    que = deque([[R, G, B]])
    count = 0
    flag = 0
    visited = set([])

    while que:
        for i in range(len(que)):
            R, G, B = que.popleft()

            if ' '.join(map(str, sorted([R, G, B]))) in visited:
                continue
            
            visited.add(' '.join(map(str, sorted([R, G, B]))))

            if R < 0 or G < 0 or B < 0:
                continue

            if R == N or G == N or B == N:
                print(count)
                comp[' '.join(map(str, sorted([R, G, B])))] = count
                flag = 1
                break
            
            if G > 0 and B > 0:
                que.append(sorted([R+2, G-1, B-1]))
            if B > 0 and R > 0:
                que.append(sorted([R-1, G + 2, B - 1]))
            if R > 0 and G > 0:
                que.append(sorted([R - 1, G - 1, B + 2]))

        if flag == 1:
            break

        count += 1

    if flag == 0:     
        print(-1)

    
    
