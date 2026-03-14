# O(n) O(n)
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        t = 3 * (1 << (n-1))
        if k > t:
            return ""
        res = []
        k -= 1
        for i in range(n):
            if i == 0:
                cc = list("abc")
            else:
                cc = [c for c in "abc" if c != res[-1]]
            b = 1 << (n - 1 - i)
            for c in cc:
                if k < b:
                    res.append(c)
                    break
                k -= b
        return ''.join(res)
        
# # O(3 * 2^(n-1) * n) O(3 * 2^(n-1) * n)
# class Solution:
#     def getHappyString(self, n: int, k: int) -> str:
#         t = 3 * (1 << (n-1))
#         if k > t:
#             return ""
#         res = []
#         def bt(path):
#             if len(path) == n:
#                 res.append(''.join(path))
#                 return
#             for c in 'abc':
#                 if path and path[-1] == c:
#                     continue
#                 path.append(c)
#                 bt(path)
#                 path.pop()
#         bt([])
#         return res[k - 1] if k <= len(res) else ""
