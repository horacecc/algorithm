# O(n) O(1)
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = cnt = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cnt += 1
                res = max(res, cnt)
            else:
                cnt = 1
        return res

# # O(n) O(n)
# class Solution:
#     def findLengthOfLCIS(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         n = len(nums)
#         dp = [1] * n
#         for i in range(1, n):
#             if nums[i] > nums[i - 1]:
#                 dp[i] = dp[i - 1] + 1
#         return max(dp)

# # O(n^2) O(1)
# class Solution:
#     def findLengthOfLCIS(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         res = 1
#         for i in range(len(nums)):
#             cnt = 1
#             for j in range(i + 1, len(nums)):
#                 if nums[j] > nums[j - 1]:
#                     cnt += 1
#                 else:
#                     break
#             res = max(res, cnt)
#         return res
