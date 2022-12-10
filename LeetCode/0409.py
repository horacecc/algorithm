# O(n) O(1)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        ss = set()
        res = 0
        for c in s:
            if c in ss:
                ss.remove(c)
                res += 2
            else:
                ss.add(c)
        return res + (1 if ss else 0)

# # O(n) O(n)
# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         cnt = {}
#         for c in s:
#             cnt[c] = cnt.get(c, 0) + 1
#         res = 0
#         odd = 0
#         for v in cnt.values():
#             if v % 2 == 0:
#                 res += v
#             else:
#                 res += v - 1
#                 odd = 1
#         return res + odd
