# O(n * k) O(n * k)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - ord('a')] += 1
            k = tuple(cnt)
            if k not in d:
                d[k] = []
            d[k].append(s)
        return list(d.values())

# # O(n * k log k) O(n * k)
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         d = {}
#         for s in strs:
#             k = tuple(sorted(s))
#             if k not in d:
#                 d[k] = []
#             d[k].append(s)
#         return list(d.values())
