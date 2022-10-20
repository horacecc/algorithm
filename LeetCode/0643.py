# O(n) O(1)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        now_sum = sum(nums[:k])
        max_sum = now_sum
        for i in range(len(nums) - k):
            now_sum += nums[i + k] - nums[i]
            max_sum = max(max_sum, now_sum)
        return max_sum / k

