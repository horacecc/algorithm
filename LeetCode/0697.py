# O(n) O(n)
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cnt = {}
        first = {}
        last = {}
        for i, x in enumerate(nums):
            cnt[x] = cnt.get(x, 0) + 1
            if x not in first:
                first[x] = i
            last[x] = i
        deg = max(cnt.values())
        res = len(nums)
        for x in cnt:
            if cnt[x] == deg:
                res = min(res, last[x] - first[x] + 1)
        return res

# # O(n^2) O(n)
# class Solution:
#     def findShortestSubArray(self, nums: List[int]) -> int:
#         cnt = {}
#         for x in nums:
#             cnt[x] = cnt.get(x, 0) + 1
#         deg = max(cnt.values())
#         res = len(nums)
#         for x in cnt:
#             if cnt[x] == deg:
#                 l = nums.index(x)
#                 r = len(nums) - 1 - nums[::-1].index(x)
#                 res = min(res, r - l + 1)
#         return res
