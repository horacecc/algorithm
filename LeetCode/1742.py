# O(n) O(1)
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        cnt = [0] * 46
        for i in range(lowLimit, highLimit + 1):
            s = 0
            t = i
            while t:
                s += t % 10
                t //= 10
            cnt[s] += 1
        return max(cnt)

# # O(n) O(n)
# class Solution:
#     def countBalls(self, lowLimit: int, highLimit: int) -> int:
#         cnt = {}
#         for i in range(lowLimit, highLimit + 1):
#             s = 0
#             while i:
#                 s += i % 10
#                 i //= 10
#             cnt[s] = cnt.get(s, 0) + 1
#         return max(cnt.values())
