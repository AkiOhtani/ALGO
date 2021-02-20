class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        left = [0] if not left else left
        right = [n] if not right else right
        return max(max(left), n-min(right))