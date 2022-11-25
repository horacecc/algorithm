# O(log n) O(1)
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        neg = num < 0
        num = abs(num)
        d = []
        while num:
            d.append(num % 7)
            num //= 7
        return ("-" if neg else "") + "".join(map(str, d[::-1]))

# # O(log n) O(log n)
# class Solution:
#     def convertToBase7(self, num: int) -> str:
#         if num == 0:
#             return "0"
#         neg = num < 0
#         num = abs(num)
#         res = ""
#         while num:
#             res = str(num % 7) + res
#             num //= 7
#         return "-" + res if neg else res
