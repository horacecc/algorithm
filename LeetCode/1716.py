# O(1) O(1)
class Solution:
    def totalMoney(self, n: int) -> int:
        w = n // 7
        d = n % 7
        full = w * 28 + 7 * w * (w - 1) // 2
        extra = d * (w + 1) + d * (d - 1) // 2
        return full + extra

# # O(n) O(1)
# class Solution:
#     def totalMoney(self, n: int) -> int:
#         res = 0
#         for i in range(n):
#             w = i // 7
#             d = i % 7
#             res += w + d + 1
#         return res
