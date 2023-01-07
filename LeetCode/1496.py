# O(n) O(n)
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        seen = {(0, 0)}
        d = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        for c in path:
            dx, dy = d[c]
            x += dx
            y += dy
            if (x, y) in seen:
                return True
            seen.add((x, y))
        return False
