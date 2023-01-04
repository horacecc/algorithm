# O(32) O(1)
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res

# # O(n) O(n)
# class Solution:
#     def reverseBits(self, n: int) -> int:
#         return int(bin(n)[2:].zfill(32)[::-1], 2)
