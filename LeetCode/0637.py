# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) O(n)
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        res = []
        q = [root]
        while q:
            s = 0
            n = len(q)
            nq = []
            for node in q:
                s += node.val
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            res.append(s / n)
            q = nq
        return res
