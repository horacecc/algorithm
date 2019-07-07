class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_maxval = [max(row) for row in grid]
        col_maxval = [max(col) for col in zip(*grid)]

        return sum(min(row_maxval[r], col_maxval[c]) - val
                   for r, row in enumerate(grid)
                   for c, val in enumerate(row))

