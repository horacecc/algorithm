# O(n) O(1)
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = 0
        for p in position:
            if p % 2:
                odd += 1
        return min(odd, len(position) - odd)

# # O(n log n) O(n)
# class Solution:
#     def minCostToMoveChips(self, position: List[int]) -> int:
#         odd = sum(1 for p in position if p % 2 == 1)
#         even = len(position) - odd
#         return min(odd, even)
