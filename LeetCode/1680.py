# O(n) O(1)
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = 0
        bits = 0
        MOD = 10**9 + 7
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                bits += 1
            res = ((res << bits) | i) % MOD
        return res

# # O(n log n) O(1)
# class Solution:
#     def concatenatedBinary(self, n: int) -> int:
#         res = 0
#         MOD = 10**9 + 7
#         for i in range(1, n + 1):
#             res = ((res << i.bit_length()) | i) % MOD
#         return res

# # O(n log n) O(n)
# class Solution:
#     def concatenatedBinary(self, n: int) -> int:
#         s = ""
#         for i in range(1, n + 1):
#             s += bin(i)[2:]
#         return int(s, 2) % (10**9 + 7)
