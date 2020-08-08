N = int(input())

stack = [int(input())]

for i in range(N-1):
    w = int(input())
    if max(stack) < w:
        stack.append(w)
        continue
    for j in range(len(stack)):
        if w <= stack[j]:
            stack[j] = w
            break
    stack.sort()
print(stack)
print(len(stack))