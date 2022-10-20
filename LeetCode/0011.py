# O(n) O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            res = max(res, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res

# # O(n^2) O(1)
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         res = 0
#         for i in range(len(height)):
#             for j in range(i + 1, len(height)):
#                 res = max(res, (j - i) * min(height[i], height[j]))
#         return res

# # O(n^2) O(1)
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         res = 0
#         for i in range(len(height)):
#             for j in range(len(height)):
#                 res = max(res, (j - i) * min(height[i], height[j]))
#         return res

