# O(m*n*k^2*log(k)) O(k^2)
class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        res = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                nums = sorted(grid[x][y] \
                    for x in range(i, i + k) \
                    for y in range(j, j + k) \
                )
                mn = float('inf')
                for t in range(1, len(nums)):
                    if nums[t] != nums[t - 1]:
                        mn = min(mn, nums[t] - nums[t - 1])
                res[i][j] = mn if mn != float('inf') else 0
        
        return res
