from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        
        for word in words:
            char_count = Counter(list(chars))
            boolean = True
            for char in word:
                char_count[char] -= 1
                if char_count[char] < 0:
                    boolean = False
            if boolean:
                count += len(word)
        return count