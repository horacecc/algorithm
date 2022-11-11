# O(n) O(n)
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        cnt = [0] * 1001
        for i in range(len(target)):
            cnt[target[i]] += 1
            cnt[arr[i]] -= 1
        return all(x == 0 for x in cnt)

# # O(n) O(n)
# class Solution:
#     def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
#         return sorted(target) == sorted(arr)
