# O(n) O(1)
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        for i in range(2):
            cnt = {}
            for j in range(i, len(s1), 2):
                cnt[s1[j]] = cnt.get(s1[j], 0) + 1
                cnt[s2[j]] = cnt.get(s2[j], 0) - 1
            if any(v != 0 for v in cnt.values()):
                return False
        return True

# # O(n log n) O(n)
# class Solution:
#     def checkStrings(self, s1: str, s2: str) -> bool:
#         for i in range(2):
#             if sorted(s1[i::2]) != sorted(s2[i::2]):
#                 return False
#         return True
