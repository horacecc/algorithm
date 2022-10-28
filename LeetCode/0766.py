# O(n*m) O(1)
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n, m = len(matrix), len(matrix[0])
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True

# # O(n*m) O(m)
# class Solution:
#     def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
#         n, m = len(matrix), len(matrix[0])
#         prev = matrix[0]
#         for i in range(1, n):
#             for j in range(1, m):
#                 if matrix[i][j] != prev[j-1]:
#                     return False
#             prev = matrix[i]
#         return True

# # O(n*m) O(n*m)
# class Solution:
#     def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
#         n, m = len(matrix), len(matrix[0])
#         d = {}
#         for i in range(n):
#             for j in range(m):
#                 k = i - j
#                 if k in d:
#                     if d[k] != matrix[i][j]:
#                         return False
#                 else:
#                     d[k] = matrix[i][j]
#         return True
