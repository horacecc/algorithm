from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx = 0
        prefixGcd = []
        for n in nums:
            mx = max(mx, n)
            prefixGcd.append(gcd(mx, n))
        prefixGcd.sort()

        res = 0
        l = 0
        r = len(nums) - 1
        while l < r:
            res += gcd(prefixGcd[l], prefixGcd[r])
            l += 1
            r -= 1
        return res
