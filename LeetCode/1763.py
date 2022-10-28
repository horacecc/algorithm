# O(n) O(n)
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        for i, c in enumerate(s):
            if c.lower() not in s or c.upper() not in s:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                return left if len(left) >= len(right) else right
        return s

# # O(n^2) O(n)
# class Solution:
#     def longestNiceSubstring(self, s: str) -> str:
#         res = ""
#         n = len(s)
#         for i in range(n):
#             for j in range(i+2, n+1):
#                 sub = s[i:j]
#                 if all(c.lower() in sub and c.upper() in sub for c in sub):
#                     if len(sub) > len(res):
#                         res = sub
#         return res

