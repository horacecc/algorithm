# O(log n) O(1)
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        mask = 1
        while mask <= n:
            mask <<= 1
        return (mask - 1) ^ n

# # O(log n) O(log n)
# class Solution:
#     def bitwiseComplement(self, n: int) -> int:
#         if n == 0:
#             return 1
#         b = bin(n)[2:]
#         return int(''.join('1' if c == '0' else '0' for c in b), 2)
