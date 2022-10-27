# O(n^2) O(1)
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    res += 2 + 4 * grid[i][j]
                if i:
                    res -= 2 * min(grid[i][j], grid[i-1][j])
                if j:
                    res -= 2 * min(grid[i][j], grid[i][j-1])
        return res

# # O(n^2) O(1)
# class Solution:
#     def surfaceArea(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         res = 0
#         for i in range(n):
#             for j in range(n):
#                 v = grid[i][j]
#                 if v > 0:
#                     res += 2 + 4 * v
#                     if i > 0:
#                         res -= min(v, grid[i-1][j]) * 2
#                     if j > 0:
#                         res -= min(v, grid[i][j-1]) * 2
#         return res

# # O(n^2) O(n)
# class Solution:
#     def surfaceArea(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         res = 0
#         for i in range(n):
#             for j in range(n):
#                 if grid[i][j] > 0:
#                     res += 2
#                     for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
#                         ni, nj = i + di, j + dj
#                         if 0 <= ni < n and 0 <= nj < n:
#                             res += max(grid[i][j] - grid[ni][nj], 0)
#                         else:
#                             res += grid[i][j]
#         return res
