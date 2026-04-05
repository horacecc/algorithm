# O(n) O(1)
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        for move in moves:
            match move:
                case "R":
                    x += 1
                case "L":
                    x -= 1
                case "U":
                    y += 1
                case "D":
                    y -= 1
        return x == 0 and y == 0

# # O(n) O(1)
# class Solution:
#     def judgeCircle(self, moves: str) -> bool:
#         d = {'U': 1j, 'D': -1j, 'L': -1, 'R': 1}
#         return sum(d[m] for m in moves) == 0

# # O(n) O(n)
# class Solution:
#     def judgeCircle(self, moves: str) -> bool:
#         return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')
