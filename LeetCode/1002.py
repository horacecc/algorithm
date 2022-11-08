# O(n) O(1)
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = [float('inf')] * 26
        for w in words:
            t = [0] * 26
            for c in w:
                t[ord(c) - 97] += 1
            for i in range(26):
                cnt[i] = min(cnt[i], t[i])
        res = []
        for i in range(26):
            res += [chr(i + 97)] * cnt[i]
        return res

# # O(n) O(n)
# class Solution:
#     def commonChars(self, words: List[str]) -> List[str]:
#         cnt = Counter(words[0])
#         for w in words[1:]:
#             cnt &= Counter(w)
#         return list(cnt.elements())

