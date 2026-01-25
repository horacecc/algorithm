# O(n log n) O(1)
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        nums.sort() # O(n log n)
        min_score = float('inf')
        
        for i in range(len(nums) - k + 1): # O(n)
            min_score = min(min_score, nums[i + k - 1] - nums[i])
        
        return min_score

# # O(n log n) O(1)
# class Solution:
#     def minimumDifference(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))

