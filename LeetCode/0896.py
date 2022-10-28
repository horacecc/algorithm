# O(n) O(1)
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = dec = True
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dec = False
            elif nums[i] < nums[i-1]:
                inc = False
            if not inc and not dec:
                return False
        return True

# # O(n) O(n)
# class Solution:
#     def isMonotonic(self, nums: List[int]) -> bool:
#         inc = dec = True
#         for i in range(1, len(nums)):
#             if nums[i] > nums[i-1]:
#                 dec = False
#             if nums[i] < nums[i-1]:
#                 inc = False
#         return inc or dec
