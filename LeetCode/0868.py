# O(log n) O(1)
class Solution:
    def binaryGap(self, n: int) -> int:
        res = 0
        prev = -1
        i = 0
        while n:
            if n & 1:
                if prev != -1:
                    res = max(res, i - prev)
                prev = i
            n >>= 1
            i += 1
        return res

# # O(n) O(n)
# class Solution:
#     def binaryGap(self, n: int) -> int:
#         b = bin(n)[2:]
#         res = 0
#         prev = -1
#         for i, c in enumerate(b):
#             if c == '1':
#                 if prev != -1:
#                     res = max(res, i - prev)
#                 prev = i
#         return res

# # O(n^2) O(n)
# class Solution:
#     def binaryGap(self, n: int) -> int:
#         b = bin(n)[2:]
#         idx = [i for i, c in enumerate(b) if c == '1']
#         if len(idx) < 2:
#             return 0
#         return max(idx[i+1] - idx[i] for i in range(len(idx)-1))
