# O(n) O(1)
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = {'U': 1j, 'D': -1j, 'L': -1, 'R': 1}
        return sum(d[m] for m in moves) == 0

# # O(n) O(n)
# class Solution:
#     def judgeCircle(self, moves: str) -> bool:
#         return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')
