# O(n * m) O(m)
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = 'aeiouAEIOU'
        res = []
        for i, w in enumerate(sentence.split(), 1):
            res.append((w if w[0] in vowels else w[1:] + w[0]) + 'ma' + 'a' * i)
        return ' '.join(res)
