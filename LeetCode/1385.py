# O((n + m) log m) O(1)
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        res = 0
        for x in arr1:
            lo, hi = 0, len(arr2)
            while lo < hi:
                m = (lo + hi) // 2
                if arr2[m] < x - d:
                    lo = m + 1
                else:
                    hi = m
            if lo == len(arr2) or abs(arr2[lo] - x) > d:
                if lo == 0 or abs(arr2[lo - 1] - x) > d:
                    res += 1
        return res

# # O(n * m) O(1)
# class Solution:
#     def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
#         res = 0
#         for x in arr1:
#             valid = True
#             for y in arr2:
#                 if abs(x - y) <= d:
#                     valid = False
#                     break
#             if valid:
#                 res += 1
#         return res
