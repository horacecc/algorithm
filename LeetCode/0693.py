# O(1) O(1)
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n ^ (n >> 1)
        return x & (x + 1) == 0

# # O(log n) O(1)
# class Solution:
#     def hasAlternatingBits(self, n: int) -> bool:
#         prev = n & 1
#         n >>= 1
#         while n:
#             curr = n & 1
#             if curr == prev:
#                 return False
#             prev = curr
#             n >>= 1
#         return True

# # O(log n) O(log n)
# class Solution:
#     def hasAlternatingBits(self, n: int) -> bool:
#         s = bin(n)[2:]
#         for i in range(1, len(s)):
#             if s[i] == s[i-1]:
#                 return False
#         return True
