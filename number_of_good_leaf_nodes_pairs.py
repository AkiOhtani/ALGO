# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node):
            if not node:
                return []
            left = dfs(node.left)
            right = dfs(node.right)

            for l in left:
                for r in right:
                    if l[1] + r[1] <= distance:
                        self.res += 1
            if left:
                left = list(map(lambda l: [l[0], l[1]+1], left))
            if right:
                right = list(map(lambda r: [r[0], r[1]+1], right))

            return [[node.val, 1]] + left + right if not left and not right else left + right
        
        self.res = 0
        dfs(root)
        return self.res