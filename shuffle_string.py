class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [None for num in indices]
        for index, c in zip(indices, s):
            res[index] = c
        return ''.join(res)