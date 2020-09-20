from queue import deque
from sys import maxsize

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        que = deque([(0, 0, grid[0][0])])
        maxprod = -maxsize
        while que:
            row, col, prod = que.popleft()
            if (row, col) == (len(grid) - 1, len(grid[0]) - 1):
                maxprod = max(maxprod, prod)
                continue
            if prod == 0:
                maxprod = max(maxprod, 0)
                continue
            for ud, lr in ((1, 0), (0, 1)):
                if not(0 <= ud + row <= len(grid) - 1 and 0 <= lr + col <= len(grid[0]) - 1):
                    continue
                #if abs(prod * grid[row+ud][col+lr]) < maxprod:
                #    continue
                que.append((row + ud, col + lr, prod * grid[row+ud][col+lr]))
        return maxprod % (10**9 + 7) if maxprod >= 0 else -1