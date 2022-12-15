# O(n log n) O(n)
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        idx = sorted(range(n), key=lambda i: -score[i])
        res = [''] * n
        for r, i in enumerate(idx):
            if r == 0:
                res[i] = "Gold Medal"
            elif r == 1:
                res[i] = "Silver Medal"
            elif r == 2:
                res[i] = "Bronze Medal"
            else:
                res[i] = str(r + 1)
        return res

# # O(n^2) O(n)
# class Solution:
#     def findRelativeRanks(self, score: List[int]) -> List[str]:
#         n = len(score)
#         res = [''] * n
#         for i in range(n):
#             rank = 1
#             for j in range(n):
#                 if score[j] > score[i]:
#                     rank += 1
#             if rank == 1:
#                 res[i] = "Gold Medal"
#             elif rank == 2:
#                 res[i] = "Silver Medal"
#             elif rank == 3:
#                 res[i] = "Bronze Medal"
#             else:
#                 res[i] = str(rank)
#         return res
