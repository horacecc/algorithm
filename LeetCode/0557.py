# O(n) O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        l = 0
        for r in range(len(s) + 1):
            if r == len(s) or s[r] == ' ':
                for i in range(r - 1, l - 1, -1):
                    res.append(s[i])
                if r < len(s):
                    res.append(' ')
                l = r + 1
        return ''.join(res)

# # O(n) O(n)
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         return ' '.join(w[::-1] for w in s.split())
