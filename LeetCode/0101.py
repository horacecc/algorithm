# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) O(n)
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([(root.left, root.right)])
        while q:
            l, r = q.popleft()
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            q.append((l.left, r.right))
            q.append((l.right, r.left))
        return True

# # O(n^2) O(n)
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True
#         left_vals = []
#         right_vals = []
#         def left_first(node):
#             if not node:
#                 left_vals.append(None)
#                 return
#             left_vals.append(node.val)
#             left_first(node.left)
#             left_first(node.right)
#         def right_first(node):
#             if not node:
#                 right_vals.append(None)
#                 return
#             right_vals.append(node.val)
#             right_first(node.right)
#             right_first(node.left)
#         left_first(root.left)
#         right_first(root.right)
#         return left_vals == right_vals
