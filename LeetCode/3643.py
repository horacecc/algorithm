# O(k ^ 2) O(m * n)
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for xx in range(k // 2):
            for yy in range(k):
                grid[x + xx][y + yy], grid[x + k - 1 - xx][y + yy] = grid[x + k - 1 - xx][y + yy], grid[x + xx][y + yy]
        return grid

# # O(m * n) O(m * n)
# class Solution:
#     def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
#         m = len(grid)
#         n = len(grid[0])
#         res = [[0] * n for _ in range(m)]

#         for xx in range(m):
#             for yy in range(n):
#                 if xx >= x and xx <= x + k - 1 and \
#                    yy >= y and yy <= y + k - 1:
#                     res[xx][yy] = grid[(x + k - 1) - (xx - x)][yy]
#                 else:
#                     res[xx][yy] = grid[xx][yy]
#         return res
