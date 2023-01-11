# O(n log n) O(n)
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        for c in s:
            if res < len(g) and c >= g[res]:
                res += 1
        return res
