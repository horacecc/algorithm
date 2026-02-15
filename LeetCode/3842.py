# O(n) O(n)
class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        c = {}
        for b in bulbs:
            c[b] = c.get(b, 0) + 1
        return sorted(b for b in c if c[b] % 2)
