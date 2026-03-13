import math

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        l = 0
        r = max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2

        while l < r:
            m = (l + r) // 2
            cnt = 0
            for t in workerTimes:
                cnt += int((-1 + math.isqrt(1 + 8 * m // t)) // 2)
            if cnt >= mountainHeight:
                r = m
            else:
                l = m + 1
        return l
