# O(n) O(n)
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        res = -1
        for num, c in cnt.items():
            if num == c:
                res = max(res, num)
        return res
