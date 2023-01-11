# O(n) O(n)
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType) // 2, len(set(candyType)))

# # O(n log n) O(n)
# class Solution:
#     def distributeCandies(self, candyType: List[int]) -> int:
#         return min(len(candyType) // 2, len(set(candyType)))
