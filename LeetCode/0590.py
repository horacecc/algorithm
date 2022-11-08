"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

# O(n) O(n)
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        stk = [(root, 0)]
        while stk:
            node, i = stk.pop()
            if i == len(node.children):
                res.append(node.val)
            else:
                stk.append((node, i + 1))
                stk.append((node.children[i], 0))
        return res

# # O(n) O(n)
# class Solution:
#     def postorder(self, root: 'Node') -> List[int]:
#         if not root:
#             return []
#         res = []
#         stk = [root]
#         while stk:
#             node = stk.pop()
#             res.append(node.val)
#             stk.extend(node.children)
#         return res[::-1]

# # O(n) O(n)
# class Solution:
#     def postorder(self, root: 'Node') -> List[int]:
#         res = []
#         def dfs(node):
#             if not node:
#                 return
#             for c in node.children:
#                 dfs(c)
#             res.append(node.val)
#         dfs(root)
#         return res
