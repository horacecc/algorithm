# O(n) O(1)
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, j = 0, 1
        while i < n and j < n:
            while i < n and nums[i] % 2 == 0:
                i += 2
            while j < n and nums[j] % 2 == 1:
                j += 2
            if i < n and j < n:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j += 2
        return nums

# # O(n log n) O(n)
# class Solution:
#     def sortArrayByParityII(self, nums: List[int]) -> List[int]:
#         even = [x for x in nums if x % 2 == 0]
#         odd = [x for x in nums if x % 2 == 1]
#         res = []
#         for i in range(len(nums) // 2):
#             res.append(even[i])
#             res.append(odd[i])
#         return res
