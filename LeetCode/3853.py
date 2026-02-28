class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        res = list(s)

        i = 0
        while i < len(res):
            j = i + 1
            next = False
            while j < i + k + 1 and j < len(res):
                if res[i] == res[j]:
                    res.pop(j)
                    next = True
                    break
                j += 1
            if next:
                i = max(0, i - k)
                continue
            i += 1
        
        return ''.join(res)
