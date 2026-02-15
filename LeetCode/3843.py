# O(n) O(n)
class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        c = {}
        for n in nums:
            c[n] = c.get(n, 0) + 1
        f = {}
        for v in c.values():
            f[v] = f.get(v, 0) + 1
        for n in nums:
            if f[c[n]] == 1:
                return n
        return -1
