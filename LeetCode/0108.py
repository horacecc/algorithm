# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) O(log n)
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            node = TreeNode(nums[mid])
            node.left = build(l, mid - 1)
            node.right = build(mid + 1, r)
            return node
        return build(0, len(nums) - 1)

# # O(n) O(n)
# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#         if not nums:
#             return None
#         mid = len(nums) // 2
#         root = TreeNode(nums[mid])
#         root.left = self.sortedArrayToBST(nums[:mid])
#         root.right = self.sortedArrayToBST(nums[mid+1:])
#         return root
