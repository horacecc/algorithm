# O(n) O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = cnt = 0
        for x in nums:
            if cnt == 0:
                res = x
            cnt += 1 if x == res else -1
        return res
        
# # O(n) O(n)
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         cnt = {}
#         for x in nums:
#             cnt[x] = cnt.get(x, 0) + 1
#             if cnt[x] > len(nums) // 2:
#                 return x

# # O(n log n) O(n)
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         return nums[len(nums) // 2]
