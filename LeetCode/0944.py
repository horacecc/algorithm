# O(n * m) O(1)
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(any(strs[i][j] < strs[i-1][j] for i in range(1, len(strs))) for j in range(len(strs[0])))

# # O(n * m) O(n * m)
# class Solution:
#     def minDeletionSize(self, strs: List[str]) -> int:
#         res = 0
#         for j in range(len(strs[0])):
#             for i in range(1, len(strs)):
#                 if strs[i][j] < strs[i-1][j]:
#                     res += 1
#                     break
#         return res
