# O(n) O(1)
class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp = 0
        count_b = 0
        for c in s:
            if c == 'b':
                count_b += 1
            else:
                dp = min(dp + 1, count_b)
        return dp
