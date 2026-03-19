# O(m*n) O(n)
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n = len(grid[0])
        res = 0
        row = [[0, 0] for _ in range(n)]

        for r in grid:
            x, y = 0, 0
            for j in range(n):
                if r[j] == 'X':
                    x += 1
                elif r[j] == 'Y':
                    y += 1
                row[j][0] += x
                row[j][1] += y
                if row[j][0] > 0 and row[j][0] == row[j][1]:
                    res += 1
        return res

# # O(m*n) O(m*n)
# class Solution:
#     def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
#         m = len(grid)
#         n = len(grid[0])

#         res = 0
#         p = [[[0, 0] for _ in range(n+1)] for _ in range(m+1)]

#         for i in range(m):
#             for j in range(n):
#                 p[i+1][j+1][0] = p[i][j+1][0] + p[i+1][j][0] \
#                                 - p[i][j][0] + (1 if grid[i][j] == 'X' else 0)
#                 p[i+1][j+1][1] = p[i][j+1][1] + p[i+1][j][1] \
#                                 - p[i][j][1] + (1 if grid[i][j] == 'Y' else 0)
#                 if p[i+1][j+1][0] > 0 and p[i+1][j+1][0] == p[i+1][j+1][1]:
#                     res += 1
#         return res
