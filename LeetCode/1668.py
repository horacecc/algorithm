# O(n * m) O(n)
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n, m = len(sequence), len(word)
        dp = [0] * n
        for i in range(m - 1, n):
            if sequence[i - m + 1:i + 1] == word:
                dp[i] = (dp[i - m] if i >= m else 0) + 1
        return max(dp) if dp else 0
