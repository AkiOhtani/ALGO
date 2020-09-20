class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        res = []
        def subsets(path):
            if len(path) == len(s):
                res.append(path)
                return
            for boolean in (True, False):
                subsets(path+[boolean])

        def boolToW(bool_list):
            pre = 0
            w_list = []
            for index, boolean in enumerate(bool_list):
                if boolean:
                    if s[pre:index+1] not in w_list:
                        w_list.append(s[pre:index+1])
                        pre = index+1
                    else:
                        return 0
            return len(w_list)
        subsets([])
        return max(1, max(map(lambda x: boolToW(x), res)))
