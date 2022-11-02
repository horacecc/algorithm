# O(n) O(1)
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        min_r = m
        min_c = n
        for op in ops:
            min_r = min(min_r, op[0])
            min_c = min(min_c, op[1])
        return min_r * min_c
