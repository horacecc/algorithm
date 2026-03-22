class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        cnt = 0
        for n in nums1:
            if n % 2:
                cnt += 1
        a1 = cnt == 0
        a2 = cnt >= 1
        return a1 or a2
