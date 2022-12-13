# O(n*m) O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_len = min(len(s) for s in strs)
        for i in range(min_len):
            c = strs[0][i]
            for s in strs:
                if s[i] != c:
                    return strs[0][:i]
        return strs[0][:min_len]

# # O(n*m) O(m)
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
#         for i in range(len(strs[0])):
#             c = strs[0][i]
#             for s in strs[1:]:
#                 if i >= len(s) or s[i] != c:
#                     return strs[0][:i]
#         return strs[0]
