# O(n) O(1)
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97}
        cnt = sum(1 for i in range(1, n + 1) if i in primes)
        res = 1
        MOD = 10 ** 9 + 7
        for i in range(1, cnt + 1):
            res = res * i % MOD
        for i in range(1, n - cnt + 1):
            res = res * i % MOD
        return res

# # O(n) O(n)
# class Solution:
#     def numPrimeArrangements(self, n: int) -> int:
#         primes = [0] * (n + 1)
#         for i in range(2, n + 1):
#             primes[i] = 1
#         for i in range(2, int(n ** 0.5) + 1):
#             if primes[i]:
#                 for j in range(i * i, n + 1, i):
#                     primes[j] = 0
        
#         cnt = sum(primes)
#         res = 1
#         MOD = 10 ** 9 + 7
#         for i in range(1, cnt + 1):
#             res = res * i % MOD
#         for i in range(1, n - cnt + 1):
#             res = res * i % MOD
#         return res
