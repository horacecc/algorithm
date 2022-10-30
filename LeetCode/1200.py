# O(n log n) O(1)
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []
        min_diff = float('inf')
        for i in range(1, len(arr)):
            d = arr[i] - arr[i-1]
            if d < min_diff:
                min_diff = d
                res = [[arr[i-1], arr[i]]]
            elif d == min_diff:
                res.append([arr[i-1], arr[i]])
        return res

# # O(n log n) O(n)
# class Solution:
#     def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
#         arr.sort()
#         diffs = []
#         for i in range(1, len(arr)):
#             diffs.append((arr[i] - arr[i-1], arr[i-1], arr[i]))
#         diffs.sort()
#         min_diff = diffs[0][0]
#         res = []
#         for d, a, b in diffs:
#             if d == min_diff:
#                 res.append([a, b])
#         return res
