# O(n) O(n)
class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = []
        for c in address:
            if c == '.':
                res.append('[.]')
            else:
                res.append(c)
        return ''.join(res)

# # O(n) O(n)
# class Solution:
#     def defangIPaddr(self, address: str) -> str:
#         return address.replace('.', '[.]')
