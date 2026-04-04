# O(rows * cols) O(n)
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        if n == 0:
            return ""
        cols = n // rows
        res = []
        for col in range(cols):
            row, cc = 0, col
            while row < rows and cc < cols:
                res.append(encodedText[row * cols + cc])
                row += 1
                cc += 1
        return ''.join(res).rstrip()
