# O(n) O(1)
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        v = set('aeiouAEIOU')
        n = len(s) // 2
        cnt = 0
        for i in range(n):
            if s[i] in v:
                cnt += 1
            if s[n + i] in v:
                cnt -= 1
        return cnt == 0
        
# # O(n) O(n)
# class Solution:
#     def halvesAreAlike(self, s: str) -> bool:
#         v = set('aeiouAEIOU')
#         n = len(s) // 2
#         a = sum(1 for c in s[:n] if c in v)
#         b = sum(1 for c in s[n:] if c in v)
#         return a == b
