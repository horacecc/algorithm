# O(n + m) O(n)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        stk = []
        for x in nums2:
            while stk and stk[-1] < x:
                d[stk.pop()] = x
            stk.append(x)
        return [d.get(x, -1) for x in nums1]

# # O(n * m) O(n)
# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         res = []
#         for x in nums1:
#             idx = nums2.index(x)
#             found = -1
#             for j in range(idx + 1, len(nums2)):
#                 if nums2[j] > x:
#                     found = nums2[j]
#                     break
#             res.append(found)
#         return res
