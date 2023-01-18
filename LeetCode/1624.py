# O(n) O(26)
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = {}
        res = -1
        for i, c in enumerate(s):
            if c in first:
                res = max(res, i - first[c] - 1)
            else:
                first[c] = i
        return res

# # O(n^2) O(1)
# class Solution:
#     def maxLengthBetweenEqualCharacters(self, s: str) -> int:
#         res = -1
#         for i in range(len(s)):
#             for j in range(i + 1, len(s)):
#                 if s[i] == s[j]:
#                     res = max(res, j - i - 1)
#         return res
