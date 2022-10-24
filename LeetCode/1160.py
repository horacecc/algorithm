# O(n) O(1)
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = [0] * 26
        for c in chars:
            chars_count[ord(c) - ord('a')] += 1
        
        result = 0
        for word in words:
            word_count = [0] * 26
            for c in word:
                word_count[ord(c) - ord('a')] += 1
            
            if all(word_count[i] <= chars_count[i] for i in range(26)):
                result += len(word)
        return result

# # O(n) O(n)
# class Solution:
#     def countCharacters(self, words: List[str], chars: str) -> int:
#         from collections import Counter
#         chars_count = Counter(chars)
#         result = 0
#         for word in words:
#             word_count = Counter(word)
#             valid = True
#             for c, cnt in word_count.items():
#                 if chars_count[c] < cnt:
#                     valid = False
#                     break
#             if valid:
#                 result += len(word)
#         return result
