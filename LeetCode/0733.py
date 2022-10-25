# O(mn) O(mn)
from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        m, n = len(image), len(image[0])
        original = image[sr][sc]
        q = deque([(sr, sc)])
        image[sr][sc] = color
        
        while q:
            r, c = q.popleft()
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == original:
                    image[nr][nc] = color
                    q.append((nr, nc))
        
        return image

# # O(mn) O(mn)
# from typing import List

# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         if image[sr][sc] == color:
#             return image
        
#         m, n = len(image), len(image[0])
#         original = image[sr][sc]
#         stack = [(sr, sc)]
        
#         while stack:
#             r, c = stack.pop()
#             if 0 <= r < m and 0 <= c < n and image[r][c] == original:
#                 image[r][c] = color
#                 stack.extend([(r+1,c), (r-1,c), (r,c+1), (r,c-1)])
        
#         return image

# # O(mn) O(mn)
# from typing import List

# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         if image[sr][sc] == color:
#             return image
        
#         m, n = len(image), len(image[0])
#         original = image[sr][sc]
        
#         def dfs(r, c):
#             if r < 0 or r >= m or c < 0 or c >= n or image[r][c] != original:
#                 return
#             image[r][c] = color
#             dfs(r+1, c)
#             dfs(r-1, c)
#             dfs(r, c+1)
#             dfs(r, c-1)
        
#         dfs(sr, sc)
#         return image
