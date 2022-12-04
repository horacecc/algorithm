# O(n) O(n)
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from math import gcd
        from functools import reduce
        cnt = Counter(deck)
        return reduce(gcd, cnt.values()) >= 2

# # O(n log n) O(n)
# class Solution:
#     def hasGroupsSizeX(self, deck: List[int]) -> bool:
#         from math import gcd
#         cnt = Counter(deck)
#         g = 0
#         for v in cnt.values():
#             g = gcd(g, v)
#         return g >= 2
