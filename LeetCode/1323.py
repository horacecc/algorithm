# O(n) O(n)
class Solution:
    def maximum69Number(self, num: int) -> int:
        s = list(str(num))
        for i in range(len(s)):
            if s[i] == '6':
                s[i] = '9'
                break
        return int(''.join(s))


# # O(n^2) O(n)
# class Solution:
#     def maximum69Number(self, num: int) -> int:
#         s = str(num)
#         res = num
#         for i in range(len(s)):
#             if s[i] == '6':
#                 candidate = int(s[:i] + '9' + s[i+1:])
#                 res = max(res, candidate)
#             elif s[i] == '9':
#                 candidate = int(s[:i] + '6' + s[i+1:])
#                 res = max(res, candidate)
#         return res

