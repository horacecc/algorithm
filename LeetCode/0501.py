# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) O(n)
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        cnt = {}
        def dfs(node):
            if not node: return
            dfs(node.left)
            cnt[node.val] = cnt.get(node.val, 0) + 1
            dfs(node.right)
        dfs(root)
        mx = max(cnt.values())
        return [k for k, v in cnt.items() if v == mx]

# # O(n) O(n)
# class Solution:
#     def findMode(self, root: Optional[TreeNode]) -> List[int]:
#         nums = []
#         def dfs(node):
#             if not node: return
#             dfs(node.left)
#             nums.append(node.val)
#             dfs(node.right)
#         dfs(root)
#         cnt = {}
#         for n in nums:
#             cnt[n] = cnt.get(n, 0) + 1
#         mx = max(cnt.values())
#         return [k for k, v in cnt.items() if v == mx]
