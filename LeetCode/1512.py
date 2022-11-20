# O(n) O(n)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = {}
        res = 0
        for n in nums:
            if n in cnt:
                res += cnt[n]
                cnt[n] += 1
            else:
                cnt[n] = 1
        return res

# # O(n^2) O(n)
# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         res = 0
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] == nums[j]:
#                     res += 1
#         return res
