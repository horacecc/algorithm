# O(n * m) O(1)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        ni, nj = i + di, j + dj
                        if ni < 0 or ni >= n or nj < 0 or nj >= m or grid[ni][nj] == 0:
                            res += 1
        return res

# # O(n * m) O(n * m)
# class Solution:
#     def islandPerimeter(self, grid: List[List[int]]) -> int:
#         n, m = len(grid), len(grid[0])
#         res = 0
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == 1:
#                     res += 4
#                     if i > 0 and grid[i - 1][j] == 1:
#                         res -= 2
#                     if j > 0 and grid[i][j - 1] == 1:
#                         res -= 2
#         return res
