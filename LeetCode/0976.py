# O(n log n) O(1)
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0

# # O(n log n) O(n)
# class Solution:
#     def largestPerimeter(self, nums: List[int]) -> int:
#         nums = sorted(nums)
#         for i in range(len(nums) - 1, 1, -1):
#             if nums[i - 2] + nums[i - 1] > nums[i]:
#                 return nums[i - 2] + nums[i - 1] + nums[i]
#         return 0
