# O(n) O(1)
class Solution:
    def countSegments(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)):
            if s[i] != ' ' and (i == 0 or s[i-1] == ' '):
                cnt += 1
        return cnt
