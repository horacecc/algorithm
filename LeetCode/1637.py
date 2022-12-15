# O(n log n) O(1)
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        res = 0
        for i in range(1, len(points)):
            res = max(res, points[i][0] - points[i - 1][0])
        return res

# # O(n log n) O(n)
# class Solution:
#     def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
#         xs = sorted(set(p[0] for p in points))
#         res = 0
#         for i in range(1, len(xs)):
#             res = max(res, xs[i] - xs[i - 1])
#         return res

# # O(n^2) O(1)
# class Solution:
#     def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
#         xs = sorted(p[0] for p in points)
#         res = 0
#         for i in range(1, len(xs)):
#             res = max(res, xs[i] - xs[i - 1])
#         return res
