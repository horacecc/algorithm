# O(n) O(1)
class Solution:
    def maxDepth(self, s: str) -> int:
        res = d = 0
        for c in s:
            d += (c == '(') - (c == ')')
            res = max(res, d)
        return res

# # O(n) O(n)
# class Solution:
#     def maxDepth(self, s: str) -> int:
#         res = d = 0
#         for c in s:
#             if c == '(':
#                 d += 1
#                 res = max(res, d)
#             elif c == ')':
#                 d -= 1
#         return res
