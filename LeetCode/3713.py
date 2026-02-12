# O(n^2) O(1)
class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            cnt = [0] * 26
            mx = v = 0
            for j in range(i, n):
                k = ord(s[j]) - 97
                cnt [k] += 1
                if cnt[k] == 1:
                    v += 1
                mx = max(mx, cnt[k])
                if mx * v == j - i + 1:
                    res = max(res, j - i + 1)
        return res
