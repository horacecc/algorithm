# O(n) O(1)
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        for i in range(n):
            if arr[i] == arr[i + n // 4]:
                return arr[i]

# # O(n) O(n)
# class Solution:
#     def findSpecialInteger(self, arr: List[int]) -> int:
#         cnt = Counter(arr)
#         n = len(arr)
#         for k, v in cnt.items():
#             if v > n // 4:
#                 return k
