# O(n) O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k
        
# # O(n^2) O(n)
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         res = []
#         for n in nums:
#             if not res or res[-1] != n:
#                 res.append(n)
#         for i in range(len(res)):
#             nums[i] = res[i]
#         return len(res)
