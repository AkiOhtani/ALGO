class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        visited = set()
        
        res = 0
        
        def dfs(i, j):
            if (i, j) in visited:
                return
            elif i < 0 or len(grid) <= i or j < 0 or len(grid[0]) <= j:
                return
            visited.add((i, j))
            
            if grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            
            for ud, lr in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                dfs(i+ud, j+lr)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res