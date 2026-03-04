# O(m * n) O(m + n)
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        r, c = len(mat), len(mat[0])
        row = [0] * r
        col = [0] * c
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
        
        res = 0
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 1 and row[i] == 1 and col[j] == 1:
                    res += 1
        return res
