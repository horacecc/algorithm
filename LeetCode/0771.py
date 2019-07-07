class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        result = 0
        for jewel in list(J):
            result += list(S).count(jewel)
        return result

