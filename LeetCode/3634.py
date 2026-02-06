# O(n) O(1)
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        
        for r in range(len(nums)):
            if nums[r] > nums[l] * k:
                l += 1
        return l

# # O(n^2) O(1)
# class Solution:
#     def minRemoval(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         n = len(nums)
#         max_keep = 0
        
#         for i in range(n):
#             left, right = i, n - 1
#             while left < right:
#                 mid = (left + right + 1) // 2
#                 if nums[mid] <= nums[i] * k:
#                     left = mid
#                 else:
#                     right = mid - 1
            
#             max_keep = max(max_keep, left - i + 1)
        
#         return n - max_keep

# # O(n^2) O(1)
# class Solution:
#     def minRemoval(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         res = float('inf')
#         n = len(nums)
#         right = n - 1

#         while right > 0:
#             left = 0
#             while left < right:
#                 if nums[left] * k >= nums[right]:
#                     res = min(res, (n - 1 - right) + left)
#                 left += 1
#             right -= 1

#         if res == float('inf'):
#             return 0

#         return res
