class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        index = (len(arr)-1) // 2
        median = arr[index]
        
        res = []
        
        for num in arr:
            res.append(((median-num)**2, num))
        
        res.sort(reverse=True)
        
        return [num[1] for num in res[:k]]