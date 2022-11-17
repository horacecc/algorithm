# O(n) O(1)
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = miss = 0
        for x in nums:
            i = abs(x) - 1
            if nums[i] < 0:
                dup = abs(x)
            else:
                nums[i] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                miss = i + 1
        return [dup, miss]

# # O(n log n) O(n)
# class Solution:
#     def findErrorNums(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         s = sorted(nums)
#         dup = miss = 0
#         for i in range(1, n):
#             if s[i] == s[i-1]:
#                 dup = s[i]
#         total = n * (n + 1) // 2
#         miss = total - sum(set(nums))
#         return [dup, miss]

# # O(n) O(n)
# class Solution:
#     def findErrorNums(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         s = sorted(nums)
#         dup = miss = 0
#         for i in range(n):
#             if i > 0 and s[i] == s[i-1]:
#                 dup = s[i]
#         for i in range(1, n+1):
#             if i not in nums:
#                 miss = i
#         return [dup, miss]
