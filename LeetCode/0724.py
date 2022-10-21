# O(n) O(1)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            total -= nums[i]
            if left_sum == total:
                return i
            left_sum += nums[i]
        return -1

# # O(n) O(1)
# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         left = 0
#         right = sum(nums[1:])
#         for i in range(len(nums)):
#             if left == right:
#                 return i
#             left += nums[i]
#             if i + 1 < len(nums):
#                 right -= nums[i + 1]
#         return -1

# # O(n^2) O(1)
# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         for i in range(len(nums)):
#             left = sum(nums[:i])
#             right = sum(nums[i + 1:])
#             if left == right:
#                 return i
#         return -1

