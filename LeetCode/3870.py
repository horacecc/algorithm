class Solution:
    def countCommas(self, n: int) -> int:
        res = 0
        d = 4
        while d <= len(str(n)) + 3:
            l = 10 ** (d - 1)
            h = 10 ** d - 1
            c = (d - 1) // 3
            count = min(n, h) - l + 1
            if count > 0:
                res += c * count
            d += 1
        return res
