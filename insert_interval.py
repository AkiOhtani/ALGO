class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not newInterval:
            return intervals
        
        if not intervals:
            return [newInterval]
        
        res = []
        
        for i in range(len(intervals)):
            if intervals[i][0] < newInterval[0]:
                res.append(intervals[i])
            else:
                break
        
        if res and newInterval[0] <= res[-1][1]:
            res[-1][1] = max(newInterval[1], res[-1][1])
        else:
            res.append(newInterval)
        
        for j in range(i, len(intervals)):
            if res[-1][1] < intervals[j][0]:
                res.append(intervals[j])
            else:
                res[-1][1] = max(intervals[j][1], res[-1][1])
            
        return res