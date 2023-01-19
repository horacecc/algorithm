# O(n log n) O(n)
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))

# # O(n^2) O(n)
# class Solution:
#     def sortByBits(self, arr: List[int]) -> List[int]:
#         def count(n):
#             cnt = 0
#             while n:
#                 cnt += n & 1
#                 n >>= 1
#             return cnt
#         return sorted(arr, key=lambda x: (count(x), x))
