# O(n) O(1)
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        for j in range(len(nums)):
            if nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums

# # O(n) O(n)
# class Solution:
#     def sortArrayByParity(self, nums: List[int]) -> List[int]:
#         a = []
#         odd = []
#         for n in nums:
#             if n % 2 == 0:
#                 a.append(n)
#             else:
#                 odd.append(n)
#         return a + odd
        
# # O(n log n) O(n)
# class Solution:
#     def sortArrayByParity(self, nums: List[int]) -> List[int]:
#         return sorted(nums, key=lambda x: x % 2)
