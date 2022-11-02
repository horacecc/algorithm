# O(n) O(1)
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = -1
        d = float('inf')
        for i, (px, py) in enumerate(points):
            if px == x or py == y:
                dist = abs(px - x) + abs(py - y)
                if dist < d:
                    d = dist
                    res = i
        return res

# # O(n^2) O(1)
# class Solution:
#     def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
#         res = -1
#         d = float('inf')
#         for i in range(len(points)):
#             px, py = points[i]
#             if px == x or py == y:
#                 dist = abs(px - x) + abs(py - y)
#                 if dist < d:
#                     d = dist
#                     res = i
#         return res
