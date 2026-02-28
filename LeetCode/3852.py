class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1

        ss = sorted(d)

        for i in ss:
            for j in ss:
                if i < j and d[i] != d[j]:
                    return [i, j]
        return [-1, -1]
