# O(m+n) O(1)
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt = 0
        i, j = m - 1, 0
        while i >= 0 and j < n:
            if grid[i][j] < 0:
                cnt += n - j
                i -= 1
            else:
                j += 1
        return cnt

# # O(m * log(n)) O(1)
# class Solution:
#     def countNegatives(self, grid: List[List[int]]) -> int:
#         cnt = 0
#         n = len(grid[0])
#         for row in grid:
#             l, r = 0, n
#             while l < r:
#                 m = (l + r) // 2
#                 if row[m] >= 0:
#                     l = m + 1
#                 else:
#                     r = m
#             cnt += n - l
#         return cnt
