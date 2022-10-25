# O(n + m) O(m)
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        count = [0] * 1001
        for boxes, units in boxTypes:
            count[units] += boxes
        res = 0
        for units in range(1000, -1, -1):
            if count[units] == 0:
                continue
            take = min(count[units], truckSize)
            res += take * units
            truckSize -= take
            if truckSize == 0:
                break
        return res

# # O(n log n) O(1)
# class Solution:
#     def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
#         boxTypes.sort(key=lambda x: -x[1])
#         res = 0
#         for boxes, units in boxTypes:
#             if truckSize <= 0:
#                 break
#             take = min(boxes, truckSize)
#             res += take * units
#             truckSize -= take
#         return res

# # O(n log n) O(n)
# class Solution:
#     def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
#         boxTypes.sort(key=lambda x: x[1])
#         res = 0
#         while truckSize > 0 and boxTypes:
#             boxes, units = boxTypes.pop()
#             take = min(boxes, truckSize)
#             res += take * units
#             truckSize -= take
#         return res
