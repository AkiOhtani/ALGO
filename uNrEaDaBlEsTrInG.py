S = input()

for index, c in enumerate(S):
    if index % 2 == 0 and S[index].isupper():
        print("No")
        exit()
    elif index % 2 == 1 and S[index].islower():
        print("No")
        exit()
print("Yes")