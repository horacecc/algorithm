# O(n) O(n)
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        t = s + s
        n = len(goal)
        lps = [0] * n
        l = 0
        for i in range(1, n):
            while l and goal[i] != goal[l]:
                l = lps[l - 1]
            if goal[i] == goal[l]:
                l += 1
            lps[i] = l
        j = 0
        for i in range(len(t)):
            while j and t[i] != goal[j]:
                j = lps[j - 1]
            if t[i] == goal[j]:
                j += 1
            if j == n:
                return True
        return False

# # O(n^2) O(n)
# class Solution:
#     def rotateString(self, s: str, goal: str) -> bool:
#         if len(s) != len(goal):
#             return False
#         for i in range(len(s)):
#             if s[i:] + s[:i] == goal:
#                 return True
#         return False
