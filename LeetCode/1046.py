# O(n log n) O(n)
import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        h = [-x for x in stones]
        heapq.heapify(h)
        while len(h) > 1:
            a = -heapq.heappop(h)
            b = -heapq.heappop(h)
            if a != b:
                heapq.heappush(h, -(a - b))
        return -h[0] if h else 0

# # O(n^2) O(n)
# class Solution:
#     def lastStoneWeight(self, stones: list[int]) -> int:
#         while len(stones) > 1:
#             stones = sorted(stones)
#             a, b = stones[-1], stones[-2]
#             stones = stones[:-2]
#             if a != b:
#                 stones.append(a - b)
#         return stones[0] if stones else 0
