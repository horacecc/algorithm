# O(m*n) O(1)
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = 0
        m = len(grid)
        n = len(grid[0])
        for r in range(m):
            for c in range(n):
                total += grid[r][c]
        
        if total % 2:
            return False
        
        equal = total // 2
        
        s = 0
        for r in range(m - 1):
            for c in range(n):
                s += grid[r][c]
            if equal == s:
                return True
        
        s = 0
        for c in range(n - 1):
            for r in range(m):
                s += grid[r][c]
            if equal == s:
                return True

        return False
