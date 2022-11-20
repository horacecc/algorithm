# O(n) O(n)
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk = []
        for c in s:
            if stk and stk[-1] == c:
                stk.pop()
            else:
                stk.append(c)
        return ''.join(stk)

# # O(n) O(n)
# class Solution:
#     def removeDuplicates(self, s: str) -> str:
#         res = []
#         for c in s:
#             if res and res[-1] == c:
#                 res.pop()
#             else:
#                 res.append(c)
#         return ''.join(res)

# # O(n^2) O(n)
# class Solution:
#     def removeDuplicates(self, s: str) -> str:
#         res = list(s)
#         while True:
#             found = False
#             i = 0
#             while i < len(res) - 1:
#                 if res[i] == res[i+1]:
#                     res.pop(i)
#                     res.pop(i)
#                     found = True
#                 else:
#                     i += 1
#             if not found:
#                 break
#         return ''.join(res)
