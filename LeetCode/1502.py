# O(n) O(n)
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        mn, mx = min(arr), max(arr)
        if (mx - mn) % (n - 1) != 0:
            return False
        d = (mx - mn) // (n - 1)
        if d == 0:
            return True
        s = set()
        for x in arr:
            if (x - mn) % d != 0:
                return False
            s.add(x)
        return len(s) == n

# # O(n log n) O(n)
# class Solution:
#     def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
#         arr.sort()
#         d = arr[1] - arr[0]
#         for i in range(2, len(arr)):
#             if arr[i] - arr[i - 1] != d:
#                 return False
#         return True
