from functools import reduce
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return reduce(lambda x, y: x + y, [[x, y] for x, y in zip(nums[:n], nums[n:])])