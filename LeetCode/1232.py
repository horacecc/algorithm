# O(n) O(1)
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        dx = coordinates[1][0] - x0
        dy = coordinates[1][1] - y0
        for x, y in coordinates[2:]:
            if dy * (x - x0) != dx * (y - y0):
                return False
        return True

# # O(n^2) O(1)
# class Solution:
#     def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
#         for i in range(2, len(coordinates)):
#             x0, y0 = coordinates[0]
#             x1, y1 = coordinates[1]
#             x2, y2 = coordinates[i]
#             if (y1 - y0) * (x2 - x0) != (y2 - y0) * (x1 - x0):
#                 return False
#         return True
