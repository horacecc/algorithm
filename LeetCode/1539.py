# O(n) O(1)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for num in arr:
            if num <= k:
                k += 1
            else:
                break
        return k

# # O(n) O(n)
# class Solution:
#     def findKthPositive(self, arr: List[int], k: int) -> int:
#         s = set(arr)
#         cnt = 0
#         num = 0
#         while cnt < k:
#             num += 1
#             if num not in s:
#                 cnt += 1
#         return num
