# O(n) O(1)
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cnt = [0] * 100
        res = 0
        for a, b in dominoes:
            k = min(a, b) * 10 + max(a, b)
            res += cnt[k]
            cnt[k] += 1
        return res

# # O(n^2) O(n)
# class Solution:
#     def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
#         cnt = 0
#         for i in range(len(dominoes)):
#             for j in range(i + 1, len(dominoes)):
#                 a, b = dominoes[i]
#                 c, d = dominoes[j]
#                 if (a == c and b == d) or (a == d and b == c):
#                     cnt += 1
#         return cnt
