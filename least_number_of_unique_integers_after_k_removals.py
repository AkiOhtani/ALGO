from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        if not arr:
            return 0
        minus = 0
        
        num_count = Counter(arr)
        
        for key, count in num_count.most_common()[::-1]:
            if k - count < 0:
                break
            k -= count
            minus -= 1
        return len(num_count) + minus