# O(n log n) O(n)
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])

# # O(n log n) O(n)
# class Solution:
#     def arrayPairSum(self, nums: List[int]) -> int:
#         nums.sort()
#         res = 0
#         for i in range(0, len(nums), 2):
#             res += nums[i]
#         return res
