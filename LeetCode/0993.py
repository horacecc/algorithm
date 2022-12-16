# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) O(n)
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = [(root, None)]
        while q:
            nxt = []
            px = py = None
            for node, p in q:
                if node.val == x:
                    px = p
                if node.val == y:
                    py = p
                if node.left:
                    nxt.append((node.left, node))
                if node.right:
                    nxt.append((node.right, node))
            if px and py:
                return px != py
            if px or py:
                return False
            q = nxt
        return False
