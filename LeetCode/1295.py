# O(n) O(1)
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            cnt = 0
            while n:
                cnt += 1
                n //= 10
            if cnt % 2 == 0:
                res += 1
        return res

# # O(n) O(n)
# class Solution:
#     def findNumbers(self, nums: List[int]) -> int:
#         return sum(1 for n in nums if len(str(n)) % 2 == 0)
