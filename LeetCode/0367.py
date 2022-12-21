# O(log n) O(1)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = num
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num

# # O(sqrt(n)) O(1)
# class Solution:
#     def isPerfectSquare(self, num: int) -> bool:
#         i = 1
#         while i * i < num:
#             i += 1
#         return i * i == num
