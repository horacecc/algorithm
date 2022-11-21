# O(n) O(n)
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        cnt = [0] * 101
        for h in heights:
            cnt[h] += 1
        res = j = 0
        for h in heights:
            while cnt[j] == 0:
                j += 1
            if h != j:
                res += 1
            cnt[j] -= 1
        return res

# # O(n) O(n)
# class Solution:
#     def heightChecker(self, heights: List[int]) -> int:
#         return sum(a != b for a, b in zip(heights, sorted(heights)))
