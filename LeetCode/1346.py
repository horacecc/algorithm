# O(n) O(n)
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()
        for x in arr:
            if 2 * x in s or (x % 2 == 0 and x // 2 in s):
                return True
            s.add(x)
        return False

# # O(n log n) O(n)
# class Solution:
#     def checkIfExist(self, arr: List[int]) -> bool:
#         arr.sort()
#         for i, x in enumerate(arr):
#             t = 2 * x
#             lo, hi = 0, len(arr) - 1
#             while lo <= hi:
#                 mid = (lo + hi) // 2
#                 if arr[mid] == t and mid != i:
#                     return True
#                 elif arr[mid] < t:
#                     lo = mid + 1
#                 else:
#                     hi = mid - 1
#         return False
