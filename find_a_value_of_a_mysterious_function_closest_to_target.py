from sys import maxsize
MAX_INT = maxsize

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        def func(l, r, dp):
            while len(dp) < r-l+1:
                dp.append(dp[-1]&arr[l+len(dp)])
            return dp[r-l]
        
        res = MAX_INT
        
        for i in range(len(arr)):
            j = i
            diff = MAX_INT
            
            dp = [arr[i]]
            
            while target <= func(i, j, dp) :
                if j == len(arr) - 1:
                    break
                j += 1
            st, ed = i, j + 1
            
            mid = (st + ed) // 2
            
            while st <= mid < ed and abs(target - func(i, mid, dp)) < diff:
                diff = abs(target - func(i, mid, dp))
                if target < func(i, mid, dp):
                    mid = (mid + 1 + ed) // 2
                elif func(i, mid, dp) < target:
                    mid = (st + mid) // 2
                else:
                    return 0
                #print("start:{}, end:{}".format(i, mid))
            res = min(res, diff)
        return res