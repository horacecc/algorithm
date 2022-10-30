# O(n) O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False

# # O(n log n) O(1)
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i - 1]:
#                 return True
#         return False

# # O(n^2) O(n)
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] == nums[j]:
#                     return True
#         return False
