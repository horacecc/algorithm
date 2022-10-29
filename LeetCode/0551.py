# O(n) O(1)
class Solution:
    def checkRecord(self, s: str) -> bool:
        a = 0
        l = 0
        for c in s:
            if c == 'A':
                a += 1
                if a >= 2:
                    return False
                l = 0
            elif c == 'L':
                l += 1
                if l >= 3:
                    return False
            else:
                l = 0
        return True

# # O(n) O(n)
# class Solution:
#     def checkRecord(self, s: str) -> bool:
#         a = s.count('A')
#         if a >= 2:
#             return False
#         return 'LLL' not in s
