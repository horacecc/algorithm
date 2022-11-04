# O(1) O(1)
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and n % 3 == 1
        
# # O(log n) O(1)
# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         if n <= 0:
#             return False
#         while n % 4 == 0:
#             n //= 4
#         return n == 1

# # O(log n) O(log n)
# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         if n <= 0:
#             return False
#         s = bin(n)[2:]
#         return s.count('1') == 1 and len(s) % 2 == 1
