# O(n) O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

# O(n) O(n)
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         length = 0
#         res = []
        
#         for i in range(len(s)):
#             if s[i] == ' ' and length != 0:
#                 res.append(s[i-length:i])
#                 length = 0
#             elif s[i] != ' ':
#                 length += 1

#         if length != 0:
#             res.append(s[len(s)-length:])

#         res.reverse()
#         return ' '.join(res)

