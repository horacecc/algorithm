# O(n) O(n)
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        n = len(s)
        first = n % k or k
        res = [s[:first]]
        for i in range(first, n, k):
            res.append(s[i:i+k])
        return '-'.join(res)

# # O(n) O(n)
# class Solution:
#     def licenseKeyFormatting(self, s: str, k: int) -> str:
#         s = s.replace('-', '').upper()
#         res = []
#         for i, c in enumerate(reversed(s)):
#             if i > 0 and i % k == 0:
#                 res.append('-')
#             res.append(c)
#         return ''.join(reversed(res))
