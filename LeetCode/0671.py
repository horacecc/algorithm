# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) O(n)
from collections import deque

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        m1, m2 = root.val, float('inf')
        q = deque([root])
        while q:
            node = q.popleft()
            if m1 < node.val < m2:
                m2 = node.val
            if node.left and node.val == m1:
                q.append(node.left)
                q.append(node.right)
        return m2 if m2 < float('inf') else -1
