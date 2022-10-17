# O(n), O(1)
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(s)

# O(n), O(n)
# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         vowels = set('aeiouAEIOU')
#         vList = [c for c in s if c in vowels]
#         res = []
#         for c in s:
#             if c in vowels:
#                 res.append(vList.pop())
#             else:
#                 res.append(c)
#         return ''.join(res)

# O(n), O(n)
# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         a = []
#         b = []
#         for i in s:
#             if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
#                 a.append(False)
#                 b.append(i)
#             else:
#                 a.append(i)
#         res = []
#         for i in a:
#             s = i
#             if not i:
#                 s = b.pop()
#             res.append(s)
#         return ''.join(res)

