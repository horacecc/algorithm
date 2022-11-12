# O(n) O(n)
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src = set(p[0] for p in paths)
        dst = set(p[1] for p in paths)
        return (dst - src).pop()

# # O(n) O(n)
# class Solution:
#     def destCity(self, paths: List[List[str]]) -> str:
#         src = set(p[0] for p in paths)
#         for p in paths:
#             if p[1] not in src:
#                 return p[1]
