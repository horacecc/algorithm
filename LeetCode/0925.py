# O(n) O(1)
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
        return i == len(name)

# # O(n) O(n)
# class Solution:
#     def isLongPressedName(self, name: str, typed: str) -> bool:
#         g1 = []
#         i = 0
#         while i < len(name):
#             j = i
#             while j < len(name) and name[j] == name[i]:
#                 j += 1
#             g1.append((name[i], j - i))
#             i = j
#         g2 = []
#         i = 0
#         while i < len(typed):
#             j = i
#             while j < len(typed) and typed[j] == typed[i]:
#                 j += 1
#             g2.append((typed[i], j - i))
#             i = j
#         if len(g1) != len(g2):
#             return False
#         for i in range(len(g1)):
#             if g1[i][0] != g2[i][0] or g1[i][1] > g2[i][1]:
#                 return False
#         return True
