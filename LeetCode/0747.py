# O(n) O(1)
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m1 = m2 = -1
        idx = 0
        for i, n in enumerate(nums):
            if n > m1:
                m2 = m1
                m1 = n
                idx = i
            elif n > m2:
                m2 = n
        return idx if m1 >= 2 * m2 else -1

# # O(n) O(n)
# class Solution:
#     def dominantIndex(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return 0
#         idx = nums.index(max(nums))
#         s = sorted(nums, reverse=True)
#         return idx if s[0] >= 2 * s[1] else -1
