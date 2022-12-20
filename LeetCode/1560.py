# O(n) O(1)
class Solution:
    def mostVisited(self, n: int, rounds: list[int]) -> list[int]:
        s, e = rounds[0], rounds[-1]
        if s <= e:
            return list(range(s, e + 1))
        return list(range(1, e + 1)) + list(range(s, n + 1))

# # O(n) O(n)
# class Solution:
#     def mostVisited(self, n: int, rounds: list[int]) -> list[int]:
#         cnt = [0] * (n + 1)
#         for i in range(len(rounds) - 1):
#             s, e = rounds[i], rounds[i + 1]
#             if s <= e:
#                 for j in range(s, e):
#                     cnt[j] += 1
#             else:
#                 for j in range(s, n + 1):
#                     cnt[j] += 1
#                 for j in range(1, e):
#                     cnt[j] += 1
#         cnt[rounds[-1]] += 1
#         mx = max(cnt)
#         return [i for i in range(1, n + 1) if cnt[i] == mx]
