# O(n) O(n)
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ban = set(banned)
        cnt = {}
        w = []
        res = ''
        mx = 0
        for c in paragraph.lower() + ' ':
            if c.isalpha():
                w.append(c)
            elif w:
                word = ''.join(w)
                w = []
                if word not in ban:
                    cnt[word] = cnt.get(word, 0) + 1
                    if cnt[word] > mx:
                        mx = cnt[word]
                        res = word
        return res
        
# # O(n * m) O(n)
# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         ban = set(banned)
#         words = []
#         w = []
#         for c in paragraph.lower():
#             if c.isalpha():
#                 w.append(c)
#             elif w:
#                 words.append(''.join(w))
#                 w = []
#         if w:
#             words.append(''.join(w))
#         cnt = {}
#         for x in words:
#             if x not in ban:
#                 cnt[x] = cnt.get(x, 0) + 1
#         return max(cnt, key=cnt.get)
