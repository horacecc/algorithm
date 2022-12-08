# O(n) O(1)
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        res = 0
        for num in range(left, right + 1):
            if bin(num).count('1') in primes:
                res += 1
        return res

# # O(n) O(n)
# class Solution:
#     def countPrimeSetBits(self, left: int, right: int) -> int:
#         def is_prime(n):
#             if n < 2:
#                 return False
#             for i in range(2, int(n**0.5) + 1):
#                 if n % i == 0:
#                     return False
#             return True
        
#         res = 0
#         for num in range(left, right + 1):
#             cnt = bin(num).count('1')
#             if is_prime(cnt):
#                 res += 1
#         return res
