# O(n) O(1)
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        prev = 0
        cur = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                res += min(prev, cur)
                prev = cur
                cur = 1
        res += min(prev, cur)
        return res

# # O(n) O(n)
# class Solution:
#     def countBinarySubstrings(self, s: str) -> int:
#         groups = []
#         cnt = 1
#         for i in range(1, len(s)):
#             if s[i] == s[i-1]:
#                 cnt += 1
#             else:
#                 groups.append(cnt)
#                 cnt = 1
#         groups.append(cnt)
#         res = 0
#         for i in range(1, len(groups)):
#             res += min(groups[i], groups[i-1])
#         return res

# # O(n^2) O(1)
# class Solution:
#     def countBinarySubstrings(self, s: str) -> int:
#         res = 0
#         n = len(s)
#         for i in range(n):
#             cnt0 = cnt1 = 0
#             for j in range(i, n):
#                 if s[j] == '0':
#                     cnt0 += 1
#                 else:
#                     cnt1 += 1
#                 if cnt0 == cnt1 and (s[i:j+1] == '0'*cnt0 + '1'*cnt1 or s[i:j+1] == '1'*cnt1 + '0'*cnt0):
#                     res += 1
#         return res
