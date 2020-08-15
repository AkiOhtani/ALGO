from collections import Counter
N = int(input())
L_dict = Counter(map(int, input().split()))
L = sorted(L_dict.keys())

count = 0

for i in range(len(L)-2):
    for j in range(i+1, len(L)-1):
        for k in range(j+1, len(L)):
            if L[k] < L[i]+L[j]:
                count += L_dict[L[k]] * L_dict[L[j]] * L_dict[L[i]]
print(count)