# O(n) O(n)
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index1 = {s: i for i, s in enumerate(list1)}
        min_sum = float('inf')
        result = []
        for j, s in enumerate(list2):
            if j > min_sum:
                break
            if s in index1:
                idx_sum = index1[s] + j
                if idx_sum < min_sum:
                    min_sum = idx_sum
                    result = [s]
                elif idx_sum == min_sum:
                    result.append(s)
        return result

# # O(n) O(n)
# class Solution:
#     def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
#         index1 = {s: i for i, s in enumerate(list1)}
#         min_sum = float('inf')
#         result = []
#         for j, s in enumerate(list2):
#             if s in index1:
#                 idx_sum = index1[s] + j
#                 if idx_sum < min_sum:
#                     min_sum = idx_sum
#                     result = [s]
#                 elif idx_sum == min_sum:
#                     result.append(s)
#         return result
