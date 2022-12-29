# O(n) O(1)
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], mx = mx, max(mx, arr[i])
        return arr

# # O(n log n) O(n)
# class Solution:
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         n = len(arr)
#         res = [0] * n
#         for i in range(n - 1):
#             res[i] = max(arr[i + 1:])
#         res[-1] = -1
#         return res
