# O(n) O(n)
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for x, c in cnt.items():
            buckets[c].append(x)
        res = []
        for i in range(len(buckets)):
            for x in sorted(buckets[i], reverse=True):
                res.extend([x] * i)
        return res

# # O(n log n) O(n)
# class Solution:
#     def frequencySort(self, nums: List[int]) -> List[int]:
#         cnt = Counter(nums)
#         return sorted(nums, key=lambda x: (cnt[x], -x))
