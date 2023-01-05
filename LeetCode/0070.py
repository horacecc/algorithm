# O(n) O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

# # O(n) O(n)
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         dp = [0] * (n + 1)
#         dp[0] = dp[1] = 1
#         for i in range(2, n + 1):
#             dp[i] = dp[i - 1] + dp[i - 2]
#         return dp[n]

# # O(2^n) O(n)
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n
#         return self.climbStairs(n - 1) + self.climbStairs(n - 2)
