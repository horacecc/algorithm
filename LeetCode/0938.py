# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) O(n)
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        stk = [root]
        while stk:
            node = stk.pop()
            if not node:
                continue
            if low <= node.val <= high:
                res += node.val
            if node.val > low:
                stk.append(node.left)
            if node.val < high:
                stk.append(node.right)
        return res

# # O(n) O(n)
# class Solution:
#     def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
#         if not root:
#             return 0
#         res = 0
#         if low <= root.val <= high:
#             res += root.val
#         if root.val > low:
#             res += self.rangeSumBST(root.left, low, high)
#         if root.val < high:
#             res += self.rangeSumBST(root.right, low, high)
#         return res
        
