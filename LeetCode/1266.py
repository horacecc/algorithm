# O(n) O(1)
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        x, y = points[0]
        for nx, ny in points[1:]:
            res += max(abs(nx - x), abs(ny - y))
            x, y = nx, ny
        return res

# # O(n) O(1)
# class Solution:
#     def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
#         res = 0
#         for i in range(1, len(points)):
#             dx = abs(points[i][0] - points[i-1][0])
#             dy = abs(points[i][1] - points[i-1][1])
#             res += max(dx, dy)
#         return res
