# O(n) O(1)
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            nums[i] = nums[i] | (nums[i + n] << 10)
        for i in range(n - 1, -1, -1):
            nums[2 * i + 1] = nums[i] >> 10
            nums[2 * i] = nums[i] & 1023
        return nums

# # O(n) O(n)
# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
#         res = []
#         for i in range(n):
#             res.append(nums[i])
#             res.append(nums[i + n])
#         return res
