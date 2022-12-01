# O(n) O(n)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []
        i = len(num) - 1
        while i >= 0 or k:
            if i >= 0:
                k += num[i]
                i -= 1
            res.append(k % 10)
            k //= 10
        return res[::-1]

# # O(n) O(n)
# class Solution:
#     def addToArrayForm(self, num: List[int], k: int) -> List[int]:
#         return list(map(int, str(int(''.join(map(str, num))) + k)))
