# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import Counter
from queue import deque

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        depth = 0
        max_sum = Counter()
        que = deque()
        que.append((root, depth))
        while que:
            node = que.popleft()
            if node[0] == None:
                continue
            depth = node[1]
            max_sum[depth] += node[0].val
            if node[0].left:
                que.append((node[0].left, depth+1))
            if node[0].right:
                que.append((node[0].right, depth+1))
                
        return max_sum.most_common()[0][0]+1