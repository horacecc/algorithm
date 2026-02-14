# O(n * k) O(n)
class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        d = {}
        for word in words:
            if len(word) < k:
                continue
            pre = word[0:k]
            if pre not in d:
                d[pre] = 0
            d[pre] += 1
        return sum(v >= 2 for v in d.values())
