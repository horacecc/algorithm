# O(n) O(n)
class Solution:
    def reformatNumber(self, number: str) -> str:
        s = "".join(c for c in number if c.isdigit())
        res = []
        n = len(s)
        i = 0
        while n - i > 4:
            res.append(s[i:i+3])
            i += 3
        if n - i == 4:
            res += [s[i:i+2], s[i+2:]]
        else:
            res.append(s[i:])
        return "-".join(res)

# # O(n) O(n)
# class Solution:
#     def reformatNumber(self, number: str) -> str:
#         s = number.replace("-", "").replace(" ", "")
#         res = []
#         i = 0
#         while len(s) - i > 4:
#             res.append(s[i:i+3])
#             i += 3
#         if len(s) - i == 4:
#             res.append(s[i:i+2])
#             res.append(s[i+2:i+4])
#         else:
#             res.append(s[i:])
#         return "-".join(res)
