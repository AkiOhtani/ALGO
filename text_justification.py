class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        if len(words) == 1:
            return [words[0] + ' ' * (maxWidth - len(words))]
        res = [[]]
        length = 0
        
        for word in words:
            if length + len(word) + len(res[-1]) - 1 >= maxWidth:
                for i in range((maxWidth - length) % max(1, len(res[-1])-1)):
                    res[-1][i] += ' '
                    length += 1
                if len(res[-1]) > 1:
                    res[-1] = (' ' * ((maxWidth - length) // max(1, len(res[-1])-1))).join(res[-1])
                else:
                    res[-1] = res[-1][0].ljust(maxWidth)
                
                res.append([word])
                length = len(word)
            else:
                length += len(word)
                res[-1].append(word)
        
        res[-1] = (' '.join(res[-1])).ljust(maxWidth)
        return res