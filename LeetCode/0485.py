# O(n) O(1)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = cnt = 0
        for x in nums:
            if x == 1:
                cnt += 1
                res = max(res, cnt)
            else:
                cnt = 0
        return res
