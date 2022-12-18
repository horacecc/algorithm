# O(n + m) O(n)
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d = {p[0]: p for p in pieces}
        res = []
        for x in arr:
            if x in d:
                res.extend(d[x])
        return res == arr

# # O(n * m) O(n)
# class Solution:
#     def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
#         i = 0
#         while i < len(arr):
#             found = False
#             for p in pieces:
#                 if p[0] == arr[i]:
#                     for x in p:
#                         if i >= len(arr) or arr[i] != x:
#                             return False
#                         i += 1
#                     found = True
#                     break
#             if not found:
#                 return False
#         return True
