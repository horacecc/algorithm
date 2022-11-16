"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

# O(n) O(n)
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        stk = [root]
        while stk:
            node = stk.pop()
            res.append(node.val)
            stk.extend(reversed(node.children))
        return res

# # O(n) O(n)
# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         res = []
#         def dfs(node):
#             if not node:
#                 return
#             res.append(node.val)
#             for c in node.children:
#                 dfs(c)
#         dfs(root)
#         return res
