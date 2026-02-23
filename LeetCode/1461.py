# O(n * k) O(n * k)
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        m = 1 << k
        if n - k + 1 < m:
            return False
        ss = set()
        for i in range(n - k + 1):
            ss.add(s[i:i + k])
            if len(ss) == m:
                return True
        return False

# # O(n * k) O(n * k)
# class Solution:
#     def hasAllCodes(self, s: str, k: int) -> bool:
#         n = len(s)
#         m = 1 << k
#         if n - k + 1 < m:
#             return False
#         ss = {s[i:i + k] for i in range(n - k + 1)}
#         return len(ss) == m

# # O(2^k * k) O(2^k * k)
# class Solution:
#     def hasAllCodes(self, s: str, k: int) -> bool:
#         for i in range(1 << k):
#             if bin(i)[2:].zfill(k) not in s:
#                 return False
#         return True
