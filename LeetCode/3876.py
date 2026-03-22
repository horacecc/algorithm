class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        cnt = 0
        min_odd = float('inf')
        min_even = float('inf')

        for n in nums1:
            if n % 2:
                cnt += 1
                min_odd = min(min_odd, n)
            else:
                min_even = min(min_even, n)

        return cnt == 0 or min_even > min_odd
        
