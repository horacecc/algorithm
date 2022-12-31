# O(n) O(1)
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        found = False
        for i in range(len(s)):
            if s[i] == '1':
                if found:
                    return False
            else:
                if i > 0 and s[i - 1] == '1':
                    found = True
        return True

# # O(n) O(1)
# class Solution:
#     def checkOnesSegment(self, s: str) -> bool:
#         return '01' not in s or s.index('01') > s.rfind('1') - s.count('1') + 1
