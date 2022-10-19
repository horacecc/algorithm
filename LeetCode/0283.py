# O(n) O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx +=1

# O(n) O(n)
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         x = []
#         for num in nums:
#             if num != 0:
#                 x.append(num)
        
#         length = len(x)
#         for i in range(len(nums)):
#             if i < length:
#                 nums[i] = x[i]
#             else:
#                 nums[i] = 0

