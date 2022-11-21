# O(n) O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)

# # O(n) O(n)
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         s = set(nums)
#         for i in range(len(nums) + 1):
#             if i not in s:
#                 return i

# # O(n log n) O(n)
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         nums = sorted(nums)
#         for i in range(len(nums)):
#             if nums[i] != i:
#                 return i
#         return len(nums)
