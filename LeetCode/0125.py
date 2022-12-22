# O(n) O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
        
# # O(n) O(n)
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         t = ''.join(c.lower() for c in s if c.isalnum())
#         return t == t[::-1]
