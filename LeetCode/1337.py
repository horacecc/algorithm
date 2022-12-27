class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n = len(mat)
        arr = []
        for i in range(n):
            arr.append((sum(mat[i]), i))
        arr.sort()
        return [arr[i][1] for i in range(k)]
