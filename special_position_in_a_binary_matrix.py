from collections import Counter
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res = 0
        rcount = Counter()
        ccount = Counter()
        
        visited = set()
        
        for row in range(len(mat)):
            for col in range(len(mat[row])):
                if mat[row][col] == 1:
                    visited.add((row, col))
                    rcount[row]+=1
                    ccount[col]+=1
        for row, col in visited:
            if rcount[row] == 1 and ccount[col] == 1:
                res += 1
        return res