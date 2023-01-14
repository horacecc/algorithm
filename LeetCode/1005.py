# O(n log n) O(n)
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        while k > 0 and i < len(nums) and nums[i] < 0:
            nums[i] = -nums[i]
            i += 1
            k -= 1
        if k % 2:
            return sum(nums) - 2 * min(nums)
        return sum(nums)
