# O(n) O(n)
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = [0] * (n + 1)
        for num in nums:
            cnt[min(num, n)] += 1
        s = 0
        for x in range(n, 0, -1):
            s += cnt[x]
            if s == x:
                return x
        return -1

# # O(n log n) O(1)
# class Solution:
#     def specialArray(self, nums: List[int]) -> int:
#         nums.sort(reverse=True)
#         n = len(nums)
#         for x in range(1, n + 1):
#             if nums[x - 1] >= x and (x == n or nums[x] < x):
#                 return x
#         return -1

# # O(n^2) O(n)
# class Solution:
#     def specialArray(self, nums: List[int]) -> int:
#         n = len(nums)
#         for x in range(n + 1):
#             cnt = 0
#             for num in nums:
#                 if num >= x:
#                     cnt += 1
#             if cnt == x:
#                 return x
#         return -1
