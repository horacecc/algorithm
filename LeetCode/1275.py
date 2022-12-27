# O(n) O(1)
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        row = [0] * 3
        col = [0] * 3
        d1 = d2 = 0
        for i, (r, c) in enumerate(moves):
            v = 1 if i % 2 == 0 else -1
            row[r] += v
            col[c] += v
            if r == c:
                d1 += v
            if r + c == 2:
                d2 += v
            if abs(row[r]) == 3 or abs(col[c]) == 3 or abs(d1) == 3 or abs(d2) == 3:
                return 'A' if v == 1 else 'B'
        return 'Draw' if len(moves) == 9 else 'Pending'

# # O(n^2) O(1)
# class Solution:
#     def tictactoe(self, moves: List[List[int]]) -> str:
#         g = [['' for _ in range(3)] for _ in range(3)]
#         for i, (r, c) in enumerate(moves):
#             g[r][c] = 'X' if i % 2 == 0 else 'O'
#         for p in ['X', 'O']:
#             for i in range(3):
#                 if g[i][0] == g[i][1] == g[i][2] == p:
#                     return 'A' if p == 'X' else 'B'
#                 if g[0][i] == g[1][i] == g[2][i] == p:
#                     return 'A' if p == 'X' else 'B'
#             if g[0][0] == g[1][1] == g[2][2] == p:
#                 return 'A' if p == 'X' else 'B'
#             if g[0][2] == g[1][1] == g[2][0] == p:
#                 return 'A' if p == 'X' else 'B'
#         return 'Draw' if len(moves) == 9 else 'Pending'
