# O(n^2) O(1)
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rr = rc = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rr, rc = i, j
                    break
        cnt = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = rr + dr, rc + dc
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == 'B':
                    break
                if board[r][c] == 'p':
                    cnt += 1
                    break
                r += dr
                c += dc
        return cnt
