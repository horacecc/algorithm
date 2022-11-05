# O(n) O(n)
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        cnt = [0] * (n + 1)
        for a, b in trust:
            cnt[a] -= 1
            cnt[b] += 1
        for i in range(1, n + 1):
            if cnt[i] == n - 1:
                return i
        return -1

# # O(n) O(n)
# class Solution:
#     def findJudge(self, n: int, trust: List[List[int]]) -> int:
#         ind = [0] * (n + 1)
#         outd = [0] * (n + 1)
#         for a, b in trust:
#             outd[a] += 1
#             ind[b] += 1
#         for i in range(1, n + 1):
#             if ind[i] == n - 1 and outd[i] == 0:
#                 return i
#         return -1

# # O(n^2) O(n)
# class Solution:
#     def findJudge(self, n: int, trust: List[List[int]]) -> int:
#         trusted = set()
#         for a, b in trust:
#             trusted.add(a)
#         for i in range(1, n + 1):
#             if i not in trusted:
#                 cnt = 0
#                 for a, b in trust:
#                     if b == i:
#                         cnt += 1
#                 if cnt == n - 1:
#                     return i
#         return -1
