# O(log n) O(1)
class Solution:
    def findComplement(self, num: int) -> int:
        mask = 1
        while mask <= num:
            mask <<= 1
        return (mask - 1) ^ num

# # O(log n) O(n)
# class Solution:
#     def findComplement(self, num: int) -> int:
#         b = bin(num)[2:]
#         return int(''.join('1' if c == '0' else '0' for c in b), 2)
