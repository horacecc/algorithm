# O(n log n) O(1)
import math

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = 0
        left, right = 0, len(nums) - 1

        while left < right:
            max_sum = max(max_sum, nums[left] + nums[right])
            left += 1
            right -= 1

        return max_sum

# # O(n log n) O(1)
# import math

# class Solution:
#     def minPairSum(self, nums: List[int]) -> int:
#         nums.sort()
#         max_sum = 0
#         mid = math.ceil(len(nums) / 2) - 1
#         for i in range(mid + 1):
#             max_sum = max(max_sum, nums[mid - i] + nums[mid + i + 1])

#         return max_sum

