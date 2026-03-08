class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        n = len(nums)
        mx = n * max(nums)

        
        r = [1] * (n + 1)
        for i in range(n - 1, -1, -1):
            r[i] = r[i + 1] * nums[i]
            if r[i] > mx:
                r[i] = mx + 1

        l = 0
        for i in range(n):
            if l == r[i + 1]:
                return i
            l += nums[i]

        return -1
