# O(n * d) O(1)
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for num in range(left, right + 1):
            tmp = num
            valid = True
            while tmp:
                d = tmp % 10
                if d == 0 or num % d != 0:
                    valid = False
                    break
                tmp //= 10
            if valid:
                res.append(num)
        return res


# # O(n * d) O(n)
# class Solution:
#     def selfDividingNumbers(self, left: int, right: int) -> List[int]:
#         res = []
#         for num in range(left, right + 1):
#             s = str(num)
#             if '0' not in s and all(num % int(d) == 0 for d in s):
#                 res.append(num)
#         return res

