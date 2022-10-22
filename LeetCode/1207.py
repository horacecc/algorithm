# O(n) O(n)
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        cnt = Counter(arr)
        return len(cnt.values()) == len(set(cnt.values()))


# # O(n log n) O(n)
# class Solution:
#     def uniqueOccurrences(self, arr: List[int]) -> bool:
#         from collections import Counter
#         cnt = Counter(arr)
#         vals = sorted(cnt.values())
#         for i in range(1, len(vals)):
#             if vals[i] == vals[i - 1]:
#                 return False
#         return True

