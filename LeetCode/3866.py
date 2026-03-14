class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        n = {}
        for i in nums:
            n[i] = n.get(i, 0) + 1
        for i in nums:
            if i % 2 == 0 and n[i] == 1:
                return i
        return -1
