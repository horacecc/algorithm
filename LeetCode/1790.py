# O(n) O(1)
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append(i)
        if len(diff) == 0:
            return True
        if len(diff) == 2:
            return s1[diff[0]] == s2[diff[1]] and s1[diff[1]] == s2[diff[0]]
        return False
