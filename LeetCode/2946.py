# O(m*n) O(m*n)
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        k %= len(mat[0])
        if k == 0:
            return True

        for r in range(len(mat)):
            if r % 2:
                rr = mat[r][-k:] + mat[r][:-k]
            else:
                rr = mat[r][k:] + mat[r][:k]
            if rr != mat[r]:
                return False

        return True

# # O(m*n*n) O(m*n)
# class Solution:
#     def areSimilar(self, mat: List[List[int]], k: int) -> bool:
#         mmat = [r[:] for r in mat]
#         k %= len(mat[0])

#         for _ in range(k):
#             for r in range(len(mmat)):
#                 if r % 2:
#                     mmat[r] = [mmat[r][-1]] + mmat[r][:-1]
#                 else:
#                     mmat[r] = mmat[r][1:] + [mmat[r][0]]

#         return mmat == mat
