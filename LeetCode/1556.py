# O(n) O(n)
class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        parts = []
        while s:
            parts.append(s[-3:])
            s = s[:-3]
        return '.'.join(reversed(parts))

# # O(n) O(n)
# class Solution:
#     def thousandSeparator(self, n: int) -> str:
#         s = str(n)
#         result = []
#         for i, c in enumerate(reversed(s)):
#             if i > 0 and i % 3 == 0:
#                 result.append('.')
#             result.append(c)
#         return ''.join(reversed(result))
