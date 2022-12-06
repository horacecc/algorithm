# O(1) O(1)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0
        
# # O(log n) O(1)
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n <= 0:
#             return False
#         while n > 1:
#             if n & 1:
#                 return False
#             n >>= 1
#         return True

# # O(n) O(1)
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n <= 0:
#             return False
#         while n % 2 == 0:
#             n //= 2
#         return n == 1
