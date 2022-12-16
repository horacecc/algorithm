# O(n + m) O(m)
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cnt = [0] * 102
        for x in nums:
            cnt[x + 1] += 1
        for i in range(1, 102):
            cnt[i] += cnt[i - 1]
        return [cnt[x] for x in nums]

# # O(n log n) O(n)
# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         s = sorted(nums)
#         d = {}
#         for i, x in enumerate(s):
#             if x not in d:
#                 d[x] = i
#         return [d[x] for x in nums]

# # O(n^2) O(n)
# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         res = []
#         for i in range(len(nums)):
#             cnt = 0
#             for j in range(len(nums)):
#                 if nums[j] < nums[i]:
#                     cnt += 1
#             res.append(cnt)
#         return res
