# O(m*n) O(m*n)
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mx = [[0] * n for _ in range(m)]
        mn = [[0] * n for _ in range(m)]
        mx[0][0] = mn[0][0] = grid[0][0]

        for i in range(1, m):
            mx[i][0] = mn[i][0] = mx[i - 1][0] * grid[i][0]
        for i in range(1, n):
            mx[0][i] = mn[0][i] = mx[0][i - 1] * grid[0][i]
        
        for i in range(1, m):
            for j in range(1, n):
                a = mx[i - 1][j] * grid[i][j]
                b = mn[i - 1][j] * grid[i][j]
                c = mx[i][j - 1] * grid[i][j]
                d = mn[i][j - 1] * grid[i][j]
                mx[i][j] = max(a, b, c, d)
                mn[i][j] = min(a, b, c, d)
        
        return mx[m - 1][n - 1] % (10 ** 9 + 7) if mx[m - 1][n - 1] >= 0 else -1
