# O(n) O(1)
class Solution:
    def checkString(self, s: str) -> bool:
        first_b = False

        for c in s:
            if c == 'b':
                first_b = True
            elif c == 'a' and first_b:
                return False
        
        return True

# # O(n) O(1)
# class Solution:
#     def checkString(self, s: str) -> bool:
#         last_a = -1
#         first_b = len(s)

#         for i in range(len(s)):
#             if s[i] == 'a':
#                 last_a = i
#             elif s[i] == 'b' and first_b == len(s):
#                 first_b = i
        
#         return last_a < first_b

# # O(n) O(1)
# class Solution:
#     def checkString(self, s: str) -> bool:
#         return 'ba' not in s 
