# O(log n) O(1)
class Solution:
    def isHappy(self, n: int) -> bool:
        def get(n):
            res = 0
            while n:
                res += (n % 10) ** 2
                n //= 10
            return res
        
        slow = n
        fast = get(n)
        while fast != 1 and slow != fast:
            slow = get(slow)
            fast = get(get(fast))
        return fast == 1

# # O(n) O(n)
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         s = set()
#         while n != 1 and n not in s:
#             s.add(n)
#             res = 0
#             while n:
#                 res += (n % 10) ** 2
#                 n //= 10
#             n = res
#         return n == 1
