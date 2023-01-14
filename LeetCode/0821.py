# O(n) O(n)
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        res = [float('inf')] * n
        pos = -float('inf')
        for i in range(n):
            if s[i] == c:
                pos = i
            res[i] = i - pos
        pos = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                pos = i
            res[i] = min(res[i], pos - i)
        return res

# # O(n^2) O(1)
# class Solution:
#     def shortestToChar(self, s: str, c: str) -> List[int]:
#         res = []
#         for i in range(len(s)):
#             d = float('inf')
#             for j in range(len(s)):
#                 if s[j] == c:
#                     d = min(d, abs(i - j))
#             res.append(d)
#         return res
