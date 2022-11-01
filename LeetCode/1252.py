# O(n + m + k) O(n + m)
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row = [0] * m
        col = [0] * n
        for r, c in indices:
            row[r] += 1
            col[c] += 1
        odd_r = sum(r % 2 for r in row)
        odd_c = sum(c % 2 for c in col)
        return odd_r * (n - odd_c) + odd_c * (m - odd_r)

# # O(n * m) O(n + m)
# class Solution:
#     def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
#         row = [0] * m
#         col = [0] * n
#         for r, c in indices:
#             row[r] += 1
#             col[c] += 1
#         res = 0
#         for i in range(m):
#             for j in range(n):
#                 if (row[i] + col[j]) % 2:
#                     res += 1
#         return res

# # O(n * m) O(n * m)
# class Solution:
#     def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
#         mat = [[0] * n for _ in range(m)]
#         for r, c in indices:
#             for j in range(n):
#                 mat[r][j] += 1
#             for i in range(m):
#                 mat[i][c] += 1
#         res = 0
#         for i in range(m):
#             for j in range(n):
#                 if mat[i][j] % 2:
#                     res += 1
#         return res
