# O(n^2) O(n)
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zeros = []
        for row in grid:
            cnt = 0
            for j in range(n - 1, -1, -1):
                if row[j] == 0:
                    cnt += 1
                else:
                    break
            zeros.append(cnt)
        
        res = 0
        for i in range(n):
            need = n - 1 - i
            j = i
            while j < n and zeros[j] < need:
                j += 1
            if j == n:
                return -1
            while j > i:
                zeros[j], zeros[j - 1] = zeros[j - 1], zeros[j]
                j -= 1
                res += 1
        return res
