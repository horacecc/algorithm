class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        c1 = {}
        c2 = {}
        for n in nums1:
            c1[n] = c1.get(n, 0) + 1
        for n in nums2:
            c2[n] = c2.get(n, 0) + 1

        res = 0
        for i in set(list(c1.keys()) + list(c2.keys())):
            cc1 = c1.get(i, 0)
            cc2 = c2.get(i, 0)
            total = cc1 + cc2
            if total % 2:
                return -1
            d = cc2 - cc1
            if d > 0:
                res += d //2
        return res
