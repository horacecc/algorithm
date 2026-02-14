# O(n^2) O(n)
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [poured]
        for i in range(1, query_row + 1):
            nq = [0] * (i + 1)
            for j in range(i):
                overflow = max(0, dp[j] - 1)
                nq[j] += overflow / 2
                nq[j + 1] += overflow / 2
            dp = nq
        return min(1, dp[query_glass])

# # O(n^2) O(n^2)
# class Solution:
#     def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
#         dp = [[0] * (i + 1) for i in range(query_row + 1)]
#         dp[0][0] = poured
#         for i in range(query_row):
#             for j in range(i + 1):
#                 overflow = max(0, dp[i][j] - 1)
#                 dp[i + 1][j] += overflow / 2
#                 dp[i + 1][j + 1] += overflow / 2
#         return min(1, dp[query_row][query_glass])
