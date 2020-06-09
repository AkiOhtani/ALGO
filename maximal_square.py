class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        res = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                boolean = True
                for k in range(min(len(matrix)-i+1, len(matrix[0])-j+1)):
                    for l in range(k**2):
                        if matrix[i+l//k][j+l%k] == '0':
                            boolean = False
                            break
                    if not boolean:
                        break
                    res = max(res, k**2)
        return res