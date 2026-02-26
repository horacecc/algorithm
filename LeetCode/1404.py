# O(n) O(1)
class Solution:
    def numSteps(self, s: str) -> int:
        res = 0
        carry = 0
        for i in range(len(s) - 1, 0, -1):
            d = int(s[i]) + carry
            if d % 2 == 1:
                carry = 1
                res += 2
            else:
                res += 1
        return res + carry

# # O(n) O(n)
# class Solution:
#     def numSteps(self, s: str) -> int:
#         res = 0
#         s = list(s)
#         while len(s) > 1:
#             if s[-1] == '0':
#                 s.pop()
#             else:
#                 i = len(s) - 1
#                 while i >= 0 and s[i] == '1':
#                     s[i] = '0'
#                     i -= 1
#                 if i >= 0:
#                     s[i] = '1'
#                 else:
#                     s.insert(0, '1')
#             res += 1
#         return res
