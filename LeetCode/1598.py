# O(n) O(1)
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        d = 0
        for log in logs:
            if log == "../":
                if d > 0:
                    d -= 1
            elif log != "./":
                d += 1
        return d

# # O(n * m) O(1)
# class Solution:
#     def minOperations(self, logs: List[str]) -> int:
#         d = 0
#         for log in logs:
#             if log == "../":
#                 d = max(0, d - 1)
#             elif log == "./":
#                 pass
#             else:
#                 d += 1
#         return d
