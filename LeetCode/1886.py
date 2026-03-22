# O(n^2) O(1)
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        r1 = r2 = r3 = r4 = True
        for i in range(n):
            for j in range(n):
                if mat[n - j - 1][i] != target[i][j]:
                    r1 = False
                if mat[n - i - 1][n - j - 1] != target[i][j]:
                    r2 = False
                if mat[j][n - i - 1] != target[i][j]:
                    r3 = False
                if mat[i][j] != target[i][j]:
                    r4 = False
        return r1 or r2 or r3 or r4

# # O(n^2) O(n^2)
# class Solution:
#     def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
#         n = len(mat)
        
#         for _ in range(4):
#             r = [[0] * n for _ in range(n)]
            
#             for i in range(n):
#                 for j in range(n):
#                     r[i][j] = mat[n - j - 1][i]

#             if r == target:
#                 return True
#             mat = r

#         return False
