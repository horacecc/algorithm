# O(n) O(n)
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        res = 0
        for n in cnt:
            if n + 1 in cnt:
                res = max(res, cnt[n] + cnt[n + 1])
        return res

# # O(n log n) O(n)
# class Solution:
#     def findLHS(self, nums: List[int]) -> int:
#         nums.sort()
#         res = 0
#         l = 0
#         for r in range(len(nums)):
#             while nums[r] - nums[l] > 1:
#                 l += 1
#             if nums[r] - nums[l] == 1:
#                 res = max(res, r - l + 1)
#         return res
