# O(n) O(1)
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0
        for x in arr:
            if x & 1:
                cnt += 1
                if cnt == 3:
                    return True
            else:
                cnt = 0
        return False

# # O(n) O(1)
# class Solution:
#     def threeConsecutiveOdds(self, arr: List[int]) -> bool:
#         cnt = 0
#         for x in arr:
#             if x % 2 != 0:
#                 cnt += 1
#                 if cnt == 3:
#                     return True
#             else:
#                 cnt = 0
#         return False

# # O(n) O(1)
# class Solution:
#     def threeConsecutiveOdds(self, arr: List[int]) -> bool:
#         for i in range(len(arr) - 2):
#             if arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i+2] % 2 == 1:
#                 return True
#         return False

