# O(n) O(1)
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        cnt = sum(int(s[i]) != i % 2 for i in range(n))
        return min(cnt, n - cnt)
