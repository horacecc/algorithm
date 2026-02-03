# O(n) O(1)
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)

        p = 0
        while p + 1 < n and nums[p + 1] > nums[p]:
            p += 1
        
        if p == 0 or p >= n - 2:
            return False
        
        q = p

        while q + 1 < n and nums [q + 1] < nums [q]:
            q += 1
        
        if q == p or q >= n - 1:
            return False
        
        for i in range(q, n-1):
            if nums[i + 1] <= nums[i]:
                return False

        return True
