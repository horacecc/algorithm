# O(n) O(1)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            i = abs(n) - 1
            nums[i] = -abs(nums[i])
        return [i + 1 for i, n in enumerate(nums) if n > 0]

# # O(n) O(n)
# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         s = set(nums)
#         return [i for i in range(1, len(nums) + 1) if i not in s]

# # O(n^2) O(1)
# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         res = []
#         n = len(nums)
#         for i in range(1, n + 1):
#             if i not in nums:
#                 res.append(i)
#         return res
