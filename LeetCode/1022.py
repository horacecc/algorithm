# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) O(n)
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = 0
        stk = [(root, 0)]
        while stk:
            nd, cur = stk.pop()
            cur = (cur << 1) | nd.val
            if not nd.left and not nd.right:
                res += cur
            if nd.right:
                stk.append((nd.right, cur))
            if nd.left:
                stk.append((nd.left, cur))
        return res

# # O(n) O(n)
# class Solution:
#     def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
#         res = 0
#         def dfs(node, val):
#             nonlocal res
#             if not node:
#                 return
#             val = (val << 1) | node.val
#             if not node.left and not node.right:
#                 res += val
#                 return
#             dfs(node.left, val)
#             dfs(node.right, val)
#         dfs(root, 0)
#         return res
