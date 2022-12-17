# O(1) O(1)
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num += 2 ** 32
        h = "0123456789abcdef"
        res = ""
        while num:
            res = h[num & 15] + res
            num >>= 4
        return res

# # O(log n) O(log n)
# class Solution:
#     def toHex(self, num: int) -> str:
#         if num == 0:
#             return "0"
#         if num < 0:
#             num = num + 2 ** 32
#         h = "0123456789abcdef"
#         res = ""
#         while num:
#             res = h[num % 16] + res
#             num //= 16
#         return res
