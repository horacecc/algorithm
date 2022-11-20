# O(n * sqrt(n)) O(n)
class Solution:
    def divisorGame(self, n: int) -> bool:
        if n == 1:
            return False
        dp = [False] * (n + 1)
        for i in range(2, n + 1):
            for x in range(1, int(i**0.5) + 1):
                if i % x == 0 and not dp[i - x]:
                    dp[i] = True
                    break
        return dp[n]

# # O(2^n) O(n)
# class Solution:
#     def divisorGame(self, n: int) -> bool:
#         if n == 1:
#             return False
#         for x in range(1, n):
#             if n % x == 0 and not self.divisorGame(n - x):
#                 return True
#         return False
