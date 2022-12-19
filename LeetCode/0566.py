# O(m * n) O(1)
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        flat = [x for row in mat for x in row]
        return [flat[i * c:(i + 1) * c] for i in range(r)]

# # O(m * n) O(m * n)
# class Solution:
#     def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
#         m, n = len(mat), len(mat[0])
#         if m * n != r * c:
#             return mat
#         flat = []
#         for row in mat:
#             for x in row:
#                 flat.append(x)
#         res = []
#         for i in range(r):
#             row = []
#             for j in range(c):
#                 row.append(flat[i * c + j])
#             res.append(row)
#         return res
