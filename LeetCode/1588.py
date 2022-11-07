# O(n) O(1)
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        for i, x in enumerate(arr):
            cnt = ((i + 1) * (n - i) + 1) // 2
            res += cnt * x
        return res

# # O(n^2) O(n)
# class Solution:
#     def sumOddLengthSubarrays(self, arr: List[int]) -> int:
#         n = len(arr)
#         pre = [0] * (n + 1)
#         for i in range(n):
#             pre[i + 1] = pre[i] + arr[i]
#         res = 0
#         for i in range(n):
#             for l in range(1, n - i + 1, 2):
#                 res += pre[i + l] - pre[i]
#         return res

# # O(n^3) O(1)
# class Solution:
#     def sumOddLengthSubarrays(self, arr: List[int]) -> int:
#         n = len(arr)
#         res = 0
#         for i in range(n):
#             for l in range(1, n - i + 1, 2):
#                 for j in range(i, i + l):
#                     res += arr[j]
#         return res
