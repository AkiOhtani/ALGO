S = input()
T = input()

mindiff = len(T)

for i in range(len(S)-len(T)+1):
    diff = 0
    for j in range(len(T)):
        if S[i+j] != T[j]:
            diff += 1
    mindiff = min(mindiff, diff)
print(mindiff)

