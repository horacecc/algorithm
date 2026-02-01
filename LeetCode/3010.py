# O(n) O(1)
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        a = b = float('inf')
        for i in range(1, len(nums)):
            if nums[i] < a:
                a, b = nums[i], a
            elif nums[i] < b:
                b = nums[i]
        return nums[0] + a + b

# # O(n log n) O(n)
# class Solution:
#     def minimumCost(self, nums: List[int]) -> int:
#         t = sorted(nums[1:])
#         return nums[0] + t[0] + t[1]

# # O(n^2) O(n)
# class Solution:
#     def minimumCost(self, nums: List[int]) -> int:
#         n = len(nums)
#         res = float('inf')
#         for i in range(1, n):
#             for j in range(i + 1, n):
#                 res = min(res, nums[0] + nums[i] + nums[j])
#         return res
