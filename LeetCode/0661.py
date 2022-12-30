# O(m*n) O(1)
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        for i in range(m):
            for j in range(n):
                s = cnt = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n:
                            s += img[ni][nj] & 255
                            cnt += 1
                img[i][j] |= (s // cnt) << 8
        for i in range(m):
            for j in range(n):
                img[i][j] >>= 8
        return img

# # O(m*n) O(m*n)
# class Solution:
#     def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
#         m, n = len(img), len(img[0])
#         res = [[0] * n for _ in range(m)]
#         for i in range(m):
#             for j in range(n):
#                 s = cnt = 0
#                 for di in [-1, 0, 1]:
#                     for dj in [-1, 0, 1]:
#                         ni, nj = i + di, j + dj
#                         if 0 <= ni < m and 0 <= nj < n:
#                             s += img[ni][nj]
#                             cnt += 1
#                 res[i][j] = s // cnt
#         return res
