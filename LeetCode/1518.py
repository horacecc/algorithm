# O(1) O(1)
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles - 1) // (numExchange - 1)

# # O(log n) O(1)
# class Solution:
#     def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
#         res = numBottles
#         empty = numBottles
#         while empty >= numExchange:
#             new = empty // numExchange
#             res += new
#             empty = empty % numExchange + new
#         return res

# # O(n) O(n)
# class Solution:
#     def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
#         res = 0
#         empty = 0
#         while numBottles > 0:
#             res += numBottles
#             empty += numBottles
#             numBottles = empty // numExchange
#             empty = empty % numExchange
#         return res
