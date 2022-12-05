# O(n) O(n)
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        w = text.split()
        return [w[i + 2] for i in range(len(w) - 2) if w[i] == first and w[i + 1] == second]

# # O(n * m^2) O(n)
# class Solution:
#     def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
#         words = text.split()
#         res = []
#         for i in range(len(words) - 2):
#             if words[i] == first and words[i + 1] == second:
#                 res.append(words[i + 2])
#         return res
