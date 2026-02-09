# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) O(n)
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        
        
        def build(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            node = TreeNode(nums[mid])
            node.left = build(l, mid - 1)
            node.right = build(mid + 1, r)
            return node
        
        inorder(root)
        return build(0, len(nums) - 1)
