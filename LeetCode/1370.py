# O(n) O(26)
class Solution:
    def sortString(self, s: str) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        res = []
        while len(res) < len(s):
            for i in range(26):
                if cnt[i]:
                    res.append(chr(i + ord('a')))
                    cnt[i] -= 1
            for i in range(25, -1, -1):
                if cnt[i]:
                    res.append(chr(i + ord('a')))
                    cnt[i] -= 1
        return ''.join(res)
