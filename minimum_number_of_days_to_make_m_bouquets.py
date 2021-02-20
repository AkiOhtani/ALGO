class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        for t in range(min(bloomDay), max(bloomDay)+1):
            boolean = list(map(lambda x: x <= t, bloomDay))
            buf = m
            i = 0
            while i < len(bloomDay)-k+1:
                flag = True
                for boolean_judge in boolean[i:i+k]:
                    if not boolean_judge:
                        flag = False
                        break
                if flag:
                    buf -= 1
                    if buf == 0:
                        return t
                    i += k
                    continue
                i += 1
        return -1