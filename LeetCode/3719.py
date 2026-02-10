# O(n^2) O(n)
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            cnt = [0, 0]
            seen = set()
            for j in range(i, n):
                if nums[j] not in seen:
                    cnt[nums[j] & 1] += 1
                    seen.add(nums[j])
                if cnt[0] == cnt[1]:
                    res = max(res, j - i + 1)
        return res
