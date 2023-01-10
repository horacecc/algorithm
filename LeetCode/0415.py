# O(n) O(n)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        i, j = len(num1) - 1, len(num2) - 1
        c = 0
        while i >= 0 or j >= 0 or c:
            a = int(num1[i]) if i >= 0 else 0
            b = int(num2[j]) if j >= 0 else 0
            s = a + b + c
            res.append(str(s % 10))
            c = s // 10
            i -= 1
            j -= 1
        return ''.join(res[::-1])

# # O(n) O(n)
# class Solution:
#     def addStrings(self, num1: str, num2: str) -> str:
#         return str(int(num1) + int(num2))
