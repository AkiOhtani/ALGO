N = int(input())
judge = [[True for i in range(10)] for j in range(N)]

ans = [ '.###..#..###.###.#.#.###.###.###.###.###.',
        '.#.#.##....#...#.#.#.#...#.....#.#.#.#.#.',
        '.#.#..#..###.###.###.###.###...#.###.###.',
        '.#.#..#..#.....#...#...#.#.#...#.#.#...#.',
        '.###.###.###.###...#.###.###...#.###.###.']

numbers = []

for i in range(5):
    numbers.append(input())

for i in range(5):
    for j in range(N):
        for k in range(10):
            if judge[j][k] == True and numbers[i][4*j:4*(j+1)] != ans[i][4*k:4*(k+1)]:
                judge[j][k] = False

for i in range(N):
    for index, boolean in enumerate(judge[i]):
        if boolean:
            print(index, end='')
            break
print()