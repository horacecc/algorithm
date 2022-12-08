# O(n) O(1)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        si = sj = 0
        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == '#':
                    si += 1
                    i -= 1
                elif si > 0:
                    si -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if t[j] == '#':
                    sj += 1
                    j -= 1
                elif sj > 0:
                    sj -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1
        return True
