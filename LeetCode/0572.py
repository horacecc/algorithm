# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n+m) O(n+m)
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        from hashlib import sha256
        
        def merkle(node):
            if not node:
                return "#"
            left = merkle(node.left)
            right = merkle(node.right)
            node.hash = sha256(f"{node.val},{left},{right}".encode()).hexdigest()
            return node.hash
        
        def find(node, target):
            if not node:
                return False
            if node.hash == target:
                return True
            return find(node.left, target) or find(node.right, target)
        
        merkle(root)
        merkle(subRoot)
        return find(root, subRoot.hash)

# # O(n+m) O(n+m)
# class Solution:
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#         def serialize(node):
#             if not node:
#                 return ["#"]
#             return ["^" + str(node.val)] + serialize(node.left) + serialize(node.right)
        
#         def kmp(text, pattern):
#             lps = [0] * len(pattern)
#             j = 0
#             for i in range(1, len(pattern)):
#                 while j > 0 and pattern[i] != pattern[j]:
#                     j = lps[j - 1]
#                 if pattern[i] == pattern[j]:
#                     j += 1
#                 lps[i] = j
            
#             j = 0
#             for i in range(len(text)):
#                 while j > 0 and text[i] != pattern[j]:
#                     j = lps[j - 1]
#                 if text[i] == pattern[j]:
#                     j += 1
#                 if j == len(pattern):
#                     return True
#             return False
        
#         return kmp(serialize(root), serialize(subRoot))

# # O(n*m) O(n+m)
# class Solution:
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#         def serialize(node):
#             if not node:
#                 return "#"
#             return f"^{node.val},{serialize(node.left)},{serialize(node.right)}"
        
#         return serialize(subRoot) in serialize(root)

# # O(n*m) O(n)
# class Solution:
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#         def isSame(p, q):
#             if not p and not q:
#                 return True
#             if not p or not q:
#                 return False
#             return p.val == q.val and isSame(p.left, q.left) and isSame(p.right, q.right)
        
#         if not root:
#             return False
#         if isSame(root, subRoot):
#             return True
#         return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
