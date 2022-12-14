# O(n) O(1)
class Solution:
    def secondHighest(self, s: str) -> int:
        a = b = -1
        for c in s:
            if c.isdigit():
                n = int(c)
                if n > a:
                    b = a
                    a = n
                elif n > b and n < a:
                    b = n
        return b

# # O(n) O(n)
# class Solution:
#     def secondHighest(self, s: str) -> int:
#         d = set()
#         for c in s:
#             if c.isdigit():
#                 d.add(int(c))
#         if len(d) < 2:
#             return -1
#         d.remove(max(d))
#         return max(d)
