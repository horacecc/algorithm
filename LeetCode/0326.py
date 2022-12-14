# O(log n) O(1)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1

# # O(log n) O(log n)
# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         if n <= 0:
#             return False
#         if n == 1:
#             return True
#         return n % 3 == 0 and self.isPowerOfThree(n // 3)
