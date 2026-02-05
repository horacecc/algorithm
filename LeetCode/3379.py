# O(n) O(n)
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [nums[(i + nums[i]) % n] for i in range(n)]

# # O(n) O(n)
# class Solution:
#     def constructTransformedArray(self, nums: List[int]) -> List[int]:
#         res = []
#         n = len(nums)
#         for i in range(n):
#             if nums[i] > 0:
#                 res.append(nums[(i + nums[i]) % n])
#             elif nums[i] < 0:
#                 res.append(nums[((i + nums[i]) % n + n) % n]) 
#             else:
#                 res.append(nums[i])
#         return res
