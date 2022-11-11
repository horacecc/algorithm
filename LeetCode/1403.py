# O(n log n) O(n)
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total = sum(nums)
        res = []
        cur = 0
        for x in nums:
            if cur > total - cur:
                break
            res.append(x)
            cur += x
        return res

# # O(n^2) O(n)
# class Solution:
#     def minSubsequence(self, nums: List[int]) -> List[int]:
#         total = sum(nums)
#         res = []
#         cur = 0
#         while cur <= total - cur:
#             m = max(nums)
#             nums.remove(m)
#             res.append(m)
#             cur += m
#         return res
