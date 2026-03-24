# O(n*m) O(n*m)
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        p = [[0] * n for _ in range(m)]
        mod = 12345

        pre = 1
        for i in range(m):
            for j in range(n):
                p[i][j] = pre
                pre = (pre * grid[i][j]) % mod
        
        suf = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                p[i][j] = (p[i][j] * suf) % mod
                suf = (suf * grid[i][j]) % mod

        return p
