# O(n) O(1)
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

# # O(n) O(n)
# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#         tmp = [x for x in nums if x != val]
#         for i, x in enumerate(tmp):
#             nums[i] = x
#         return len(tmp)

# # O(n^2) O(1)
# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#         k = 0
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 for j in range(i, k, -1):
#                     nums[j], nums[j-1] = nums[j-1], nums[j]
#                 k += 1
#         return k
