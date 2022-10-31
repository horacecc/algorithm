# O(n) O(1)
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        idx = 1
        i = 0
        n = len(sentence)
        while i < n:
            j = 0
            while i + j < n and sentence[i + j] != ' ' and j < len(searchWord) and sentence[i + j] == searchWord[j]:
                j += 1
            if j == len(searchWord):
                return idx
            while i < n and sentence[i] != ' ':
                i += 1
            i += 1
            idx += 1
        return -1
        
# # O(n) O(n)
# class Solution:
#     def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
#         words = sentence.split()
#         for i, w in enumerate(words):
#             if w.startswith(searchWord):
#                 return i + 1
#         return -1
