# O(n) O(n)
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        if k == 0:
            return res
        code = code * 2
        l, r = (1, k) if k > 0 else (n + k, n - 1)
        s = sum(code[l:r + 1])
        for i in range(n):
            res[i] = s
            s -= code[l]
            s += code[r + 1]
            l += 1
            r += 1
        return res
        
# # O(n) O(n)
# class Solution:
#     def decrypt(self, code: List[int], k: int) -> List[int]:
#         n = len(code)
#         res = [0] * n
#         if k == 0:
#             return res
#         for i in range(n):
#             if k > 0:
#                 for j in range(1, k + 1):
#                     res[i] += code[(i + j) % n]
#             else:
#                 for j in range(1, -k + 1):
#                     res[i] += code[(i - j) % n]
#         return res
