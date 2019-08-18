class Solution:
    def lastSubstring(self, s: str) -> str:
        if not s:
            return s
        prev = 0
        res = [s]
        for i in range(len(s)):
            if s[prev] < s[i]:
                if res[0] < s[i:]:
                    res[0] = s[i:]
            prev = i
        return res[0]