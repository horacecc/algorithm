# O(n) O(1)
class Solution:
    def minPartitions(self, n: str) -> int:
        res = 0
        for s in n:
            res = max(res, int(s))
            if res == 9:
                return 9
        return res
