# O(n) O(1)
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        diff = 0
        res = n
        for i in range(2 * n):
            if int(s[i % n]) != i % 2:
                diff += 1
            if i >= n:
                if int(s[(i - n) % n]) != (i - n) % 2:
                    diff -= 1
            if i >= n - 1:
                res = min(res, diff, n - diff)
        
        return res

# # O(n^2) O(n)
# class Solution:
#     def minFlips(self, s: str) -> int:
#         n = len(s)
#         res = n
#         for k in range(n):
#             diff = 0
#             for i in range(n):
#                 if int(s[(i + k) % n]) != i % 2:
#                     diff += 1
#             res = min(res, diff, n - diff)
#         return res
