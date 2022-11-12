# O(m * n) O(1)
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_max_min = max(min(row) for row in matrix)
        col_min_max = min(max(col) for col in zip(*matrix))
        return [row_max_min] if row_max_min == col_min_max else []

# # O(m * n) O(1)
# class Solution:
#     def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
#         m, n = len(matrix), len(matrix[0])
#         res = []
#         for i in range(m):
#             for j in range(n):
#                 v = matrix[i][j]
#                 if v == min(matrix[i]) and v == max(matrix[k][j] for k in range(m)):
#                     res.append(v)
#         return res
