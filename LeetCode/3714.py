from collections import Counter

# O(n) O(n)
class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        
        # O(n) O(1)
        def calc1():
            res = i = 0
            while i < n:
                j = i + 1
                while j < n and s[j] == s[i]:
                    j += 1
                res = max(res, j - i)
                i = j
            return res
        
        # O(n) O(n)
        def calc2(a, b):
            res = i = 0
            while i < n:
                while i < n and s[i] != a and s[i] != b:
                    i += 1
                pos = {0: i - 1}
                d = 0
                while i < n and s[i] in (a, b):
                    d += 1 if s[i] == a else -1
                    if d in pos:
                        res = max(res, i - pos[d])
                    else:
                        pos[d] = i
                    i += 1
            return res
        
        # O(n) O(n)
        def calc3():
            pos = {(0, 0): -1}
            cnt = Counter()
            res = 0
            for i, c in enumerate(s):
                cnt[c] += 1
                k = (cnt['a'] - cnt['b'], cnt['b'] - cnt['c'])
                if k in pos:
                    res = max(res, i - pos[k])
                else:
                    pos[k] = i
            return res
        
        return max(
            calc1(),
            calc2('a', 'b'), calc2('b', 'c'), calc2('a', 'c'),
            calc3()
        )
