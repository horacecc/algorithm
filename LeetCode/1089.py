# O(n) O(1)
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        cnt = arr.count(0)
        i = n - 1
        j = n + cnt - 1
        while i < j:
            if j < n:
                arr[j] = arr[i]
            if arr[i] == 0:
                j -= 1
                if j < n:
                    arr[j] = 0
            i -= 1
            j -= 1

# # O(n) O(n)
# class Solution:
#     def duplicateZeros(self, arr: List[int]) -> None:
#         res = []
#         for x in arr:
#             res.append(x)
#             if x == 0:
#                 res.append(0)
#         for i in range(len(arr)):
#             arr[i] = res[i]
