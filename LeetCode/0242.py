# O(n) O(26)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        for c in t:
            cnt[ord(c) - ord('a')] -= 1
        return all(x == 0 for x in cnt)

# # O(n log n) O(n)
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)
