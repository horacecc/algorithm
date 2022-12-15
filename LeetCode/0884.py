# O(n * m) O(n * m)
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        cnt = Counter((s1 + " " + s2).split())
        return [w for w, c in cnt.items() if c == 1]

# # O(n * m) O(n * m)
# class Solution:
#     def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
#         w1 = s1.split()
#         w2 = s2.split()
#         c1 = {}
#         c2 = {}
#         for w in w1:
#             c1[w] = c1.get(w, 0) + 1
#         for w in w2:
#             c2[w] = c2.get(w, 0) + 1
#         res = []
#         for w in c1:
#             if c1[w] == 1 and w not in c2:
#                 res.append(w)
#         for w in c2:
#             if c2[w] == 1 and w not in c1:
#                 res.append(w)
#         return res
