# O(n log n) O(n)
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))
        rank = {v: i + 1 for i, v in enumerate(sorted_arr)}
        return [rank[x] for x in arr]
