# O(n) O(1)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums

# # O(n) O(n)
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         res = []
#         s = 0
#         for n in nums:
#             s += n
#             res.append(s)
#         return res
