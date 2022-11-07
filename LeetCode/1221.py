# O(n) O(1)
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = cnt = 0
        for c in s:
            cnt += 1 if c == 'L' else -1
            if cnt == 0:
                res += 1
        return res
        
# # O(n) O(n)
# class Solution:
#     def balancedStringSplit(self, s: str) -> int:
#         res = 0
#         stack = []
#         for c in s:
#             if stack and stack[-1] != c:
#                 stack.pop()
#             else:
#                 stack.append(c)
#             if not stack:
#                 res += 1
#         return res
