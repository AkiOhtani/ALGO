from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        
        head_dict = {c:0 for c in t}
        tail_dict = {c:0 for c in t}
        
        if s[0] in t:
            tail_dict[s[0]] += 1

        t_count = Counter(t)

        start, end = 0, 1
        
        res = [0, float('inf')]
        
        while start < end < len(s) + 1:
            flag = True

            for char, count in t_count.items():
                if tail_dict[char] - head_dict[char] < count:     
                    flag = False
                    break
            if flag:
                if res[1] - res[0] > end - start:
                    res = start, end
                if s[start] in t:
                    head_dict[s[start]] += 1
                start += 1
            else:
                if end < len(s) and s[end] in t:
                    tail_dict[s[end]] += 1
                end += 1
                
        return s[res[0]:res[1]] if res[1] != float('inf') else ""
