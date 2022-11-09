# O(n) O(n)
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        cnt = 0
        for c in s:
            if c == '(':
                if cnt > 0:
                    res.append(c)
                cnt += 1
            else:
                cnt -= 1
                if cnt > 0:
                    res.append(c)
        return ''.join(res)

# # O(n) O(n)
# class Solution:
#     def removeOuterParentheses(self, s: str) -> str:
#         res = []
#         stk = []
#         for c in s:
#             if c == '(':
#                 if stk:
#                     res.append(c)
#                 stk.append(c)
#             else:
#                 stk.pop()
#                 if stk:
#                     res.append(c)
#         return ''.join(res)
