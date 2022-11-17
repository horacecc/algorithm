# O(n log n) O(n)
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {x: i for i, x in enumerate(arr2)}
        return sorted(arr1, key=lambda x: (d.get(x, 1001), x))

# # O(n^2) O(n)
# class Solution:
#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
#         res = []
#         for x in arr2:
#             while x in arr1:
#                 res.append(x)
#                 arr1.remove(x)
#         return res + sorted(arr1)
