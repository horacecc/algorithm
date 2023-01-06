# O(n) O(1)
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        cnt = 0
        for i in range(len(bits) - 2, -1, -1):
            if bits[i] == 1:
                cnt += 1
            else:
                break
        return cnt % 2 == 0

# # O(n) O(n)
# class Solution:
#     def isOneBitCharacter(self, bits: List[int]) -> bool:
#         i = 0
#         while i < len(bits):
#             if i == len(bits) - 1:
#                 return True
#             if bits[i] == 1:
#                 i += 2
#             else:
#                 i += 1
#         return False
