class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        res = 0
        dp = [[0 for j in matrix[0]]+[0]]
        for i in range(len(matrix)):
            dp.append([0])
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[i+1].append(int(matrix[i-1][j]))
        
        for i in range(len(matrix)+1):
            for j in range(len(matrix[0])+1):
                if dp[i][j] == 1:
                    dp[i][j] = min(dp[i][j], min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1]))) + 1
                    res = max(res, dp[i][j])
        return res
                