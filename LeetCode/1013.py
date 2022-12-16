# O(n) O(1)
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        t = total // 3
        cnt = s = 0
        for i in range(len(arr) - 1):
            s += arr[i]
            if s == t:
                cnt += 1
                s = 0
                if cnt == 2:
                    return True
        return False

# # O(n^2) O(n)
# class Solution:
#     def canThreePartsEqualSum(self, arr: List[int]) -> bool:
#         n = len(arr)
#         pre = [0] * (n + 1)
#         for i in range(n):
#             pre[i + 1] = pre[i] + arr[i]
#         for i in range(1, n - 1):
#             for j in range(i + 1, n):
#                 s1 = pre[i]
#                 s2 = pre[j] - pre[i]
#                 s3 = pre[n] - pre[j]
#                 if s1 == s2 == s3:
#                     return True
#         return False
