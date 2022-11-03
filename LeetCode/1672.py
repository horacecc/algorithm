# O(n * m) O(1)
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0
        for row in accounts:
            res = max(res, sum(row))
        return res
