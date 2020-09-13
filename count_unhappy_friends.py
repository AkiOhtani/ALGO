from collections import defaultdict

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        adj_list = defaultdict(int)
        for x, y in pairs:
            adj_list[x] = y
            adj_list[y] = x
        
        res = 0
        
        for node, order in enumerate(preferences):
            for index in range(order.index(adj_list[node])):
                friend = order[index]
                if preferences[friend].index(node) < preferences[friend].index(adj_list[friend]):
                    res += 1
                    break
        return res