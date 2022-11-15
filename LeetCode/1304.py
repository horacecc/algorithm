# O(n) O(n)
class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = list(range(1, n))
        res.append(-sum(res))
        return res
