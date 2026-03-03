# O(n) O(1)
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        flip = 0
        while n > 1:
            mid = 1 << (n - 1)
            if k == mid:
                return "1" if flip % 2 == 0 else "0"
            if k > mid:
                k = (1 << n) - k
                flip += 1
            n -= 1
        return "0" if flip % 2 == 0 else "1"

# # O(n) O(n)
# class Solution:
#     def findKthBit(self, n: int, k: int) -> str:
#         if n == 1:
#             return "0"
#         mid = 1 << (n - 1)
#         if k == mid:
#             return "1"
#         if k < mid:
#             return self.findKthBit(n - 1, k)
#         return "0" if self.findKthBit(n - 1, (1 << n) - k) == "1" else "1"
