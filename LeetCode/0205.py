# O(n) O(n)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1, d2 = {}, {}
        for a, b in zip(s, t):
            if a in d1 and d1[a] != b:
                return False
            if b in d2 and d2[b] != a:
                return False
            d1[a] = b
            d2[b] = a
        return True
