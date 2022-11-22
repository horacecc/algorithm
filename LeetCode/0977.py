# O(n) O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        i, j, k = 0, n - 1, n - 1
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                res[k] = nums[i] * nums[i]
                i += 1
            else:
                res[k] = nums[j] * nums[j]
                j -= 1
            k -= 1
        return res

# # O(n log n) O(n)
# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         res = [x * x for x in nums]
#         res.sort()
#         return res

# # O(n^2) O(n)
# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         return sorted([x * x for x in nums])
