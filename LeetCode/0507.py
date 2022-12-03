# O(sqrt(n)) O(1)
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        s = 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                s += i
                if i * i != num:
                    s += num // i
            i += 1
        return s == num

# # O(sqrt(n)) O(sqrt(n))
# class Solution:
#     def checkPerfectNumber(self, num: int) -> bool:
#         if num <= 1:
#             return False
#         d = []
#         i = 1
#         while i * i <= num:
#             if num % i == 0:
#                 d.append(i)
#                 if i != 1 and i * i != num:
#                     d.append(num // i)
#             i += 1
#         return sum(d) == num
