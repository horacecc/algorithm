# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) O(n)
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        v, stk = root.val, [root]
        while stk:
            node = stk.pop()
            if node:
                if node.val != v:
                    return False
                stk.append(node.left)
                stk.append(node.right)
        return True

# # O(n) O(n)
# class Solution:
#     def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
#         v = root.val
#         q = [root]
#         while q:
#             node = q.pop()
#             if node.val != v:
#                 return False
#             if node.left:
#                 q.append(node.left)
#             if node.right:
#                 q.append(node.right)
#         return True

# # O(n) O(n)
# class Solution:
#     def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
#         def dfs(node):
#             if not node:
#                 return True
#             if node.val != root.val:
#                 return False
#             return dfs(node.left) and dfs(node.right)
#         return dfs(root)
