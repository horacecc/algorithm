# O(n) O(n)
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        nums = [0] * (n + 1)
        nums[1] = 1
        res = 1
        for i in range(2, n + 1):
            nums[i] = nums[i // 2] + (i % 2) * nums[i // 2 + 1]
            res = max(res, nums[i])
        return res
        
# # O(n^2) O(n)
# class Solution:
#     def getMaximumGenerated(self, n: int) -> int:
#         if n == 0:
#             return 0
#         nums = [0] * (n + 1)
#         nums[1] = 1
#         for i in range(2, n + 1):
#             if i % 2 == 0:
#                 nums[i] = nums[i // 2]
#             else:
#                 nums[i] = nums[i // 2] + nums[i // 2 + 1]
#         return max(nums)
