from collections import Counter
N = int(input())
anagram = Counter()
for i in range(N):
    anagram[''.join(sorted(input()))]+=1

print(int(sum(map(lambda x: x*(x-1)/2, anagram.values()))))