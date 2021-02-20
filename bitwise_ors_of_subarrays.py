class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        bitset = {0}
        res = set()
        for a in A:
            bitset = {a} | {a|num for num in bitset}
            res |= bitset
        return len(res)