# O(n * m) O(1)
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for i in range(len(encoded)):
            res.append(res[i] ^ encoded[i])
        return res

# # O(n * m) O(n * m)
# class Solution:
#     def decode(self, encoded: List[int], first: int) -> List[int]:
#         result = [first]
#         for num in encoded:
#             result.append(result[-1] ^ num)
#         return result
