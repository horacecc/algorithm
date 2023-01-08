# O(n) O(n)
class Solution:
    def reformat(self, s: str) -> str:
        d = [c for c in s if c.isdigit()]
        a = [c for c in s if c.isalpha()]
        if abs(len(d) - len(a)) > 1:
            return ""
        if len(d) < len(a):
            d, a = a, d
        res = []
        for i in range(len(a)):
            res.append(d[i])
            res.append(a[i])
        if len(d) > len(a):
            res.append(d[-1])
        return ''.join(res)
