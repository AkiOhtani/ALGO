S = input()
T = input()

count = 0

for index, c in enumerate(S):
    if T[index] != c:
        count += 1
print(count)