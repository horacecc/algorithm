# O(n) O(1)
class Solution:
    def modifyString(self, s: str) -> str:
        res = list(s)
        for i, c in enumerate(res):
            if c == '?':
                for x in 'abc':
                    if (i == 0 or res[i-1] != x) and (i == len(res)-1 or res[i+1] != x):
                        res[i] = x
                        break
        return ''.join(res)

# # O(n) O(n)
# class Solution:
#     def modifyString(self, s: str) -> str:
#         s = list(s)
#         n = len(s)
#         for i in range(n):
#             if s[i] == '?':
#                 for c in 'abc':
#                     l = s[i-1] if i > 0 else ''
#                     r = s[i+1] if i < n-1 else ''
#                     if c != l and c != r:
#                         s[i] = c
#                         break
#         return ''.join(s)
