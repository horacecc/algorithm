# O(n) O(n)
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = ""
        for i in range(len(nums)):
            if nums[i][i] == "1":
                res += "0"
            else:
                res += "1"
        return res

# # O(2^n) O(2^n)
# class Solution:
#     def findDifferentBinaryString(self, nums: List[str]) -> str:
#         n = len(nums)
#         s = set(nums)
#         for i in range(1 << n):
#             res = bin(i)[2:].zfill(n)
#             if res not in s:
#                 return res
