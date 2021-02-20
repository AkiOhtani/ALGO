from sys import maxsize

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def subsets(path, depth, index):
            if depth == 0:
                res.append(path)
            for i, c in enumerate(s[index+1:]):
                subsets(path + [c], depth - 1, index + i + 1)
        res = []
        rl_dict = Counter(s)
        subsets([], k, 0)
        min_length = maxsize
        for trio in res:
            buf = ''
            for c, count in (rl_dict - Counter(trio)).items():
                buf += c + str(count) if count > 1 else c
            min_length = min(min_length, len(buf))
        return min_length if min_length != maxsize else 0
        