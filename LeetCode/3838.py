# O(n * m) O(n)
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ''
        for word in words:
            i = 0
            for c in word:
                i += weights[ord(c) - 97]
            res += chr(96 + 26 - i % 26)

        return res
