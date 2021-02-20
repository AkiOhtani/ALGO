class Solution:
    def reorderSpaces(self, text: str) -> str:
        word_list = list(filter(lambda x: x, text.split()))
        space_count = text.count(' ')
        mid = space_count // (len(word_list) - 1) if len(word_list) > 1 else 0
        tail = space_count % (len(word_list) - 1) if len(word_list) > 1 else space_count
        return (' ' * mid).join(word_list) + ' ' * tail