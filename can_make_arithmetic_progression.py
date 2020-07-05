class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if not arr:
            return False
        arr.sort()
        diff = arr[1] - arr[0]
        
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        return True