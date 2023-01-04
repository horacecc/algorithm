# O(1) O(1)
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9

# # O(n) O(1)
# class Solution:
#     def addDigits(self, num: int) -> int:
#         while num >= 10:
#             s = 0
#             while num:
#                 s += num % 10
#                 num //= 10
#             num = s
#         return num
