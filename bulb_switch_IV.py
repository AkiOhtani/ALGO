class Solution:
    def minFlips(self, target: str) -> int:
        pre = '0'
        count = 0
        for i in range(len(target)):
            if target[i] != pre:
                pre = target[i]
                count += 1
        return count