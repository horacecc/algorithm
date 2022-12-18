# O(n) O(1)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        cnt = 0
        while xor:
            cnt += 1
            xor &= xor - 1
        return cnt

# # O(log n) O(1)
# class Solution:
#     def hammingDistance(self, x: int, y: int) -> int:
#         xor = x ^ y
#         cnt = 0
#         while xor:
#             cnt += xor % 2
#             xor //= 2
#         return cnt
