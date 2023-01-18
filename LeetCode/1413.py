# O(n) O(1)
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        cur = 0
        min_sum = 0
        for num in nums:
            cur += num
            min_sum = min(min_sum, cur)
        return 1 - min_sum

# # O(n^2) O(1)
# class Solution:
#     def minStartValue(self, nums: List[int]) -> int:
#         res = 1
#         while True:
#             cur = res
#             valid = True
#             for num in nums:
#                 cur += num
#                 if cur < 1:
#                     valid = False
#                     break
#             if valid:
#                 return res
#             res += 1
