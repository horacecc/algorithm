# O(n log n) O(n)
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        res = []
        mini = float('inf')
        arr.sort() # O(n log n)

        for i in range(len(arr) - 1): # O(n)
            mini_now = arr[i + 1] - arr[i]
            if mini_now < mini:
                mini = mini_now
                res = [[arr[i], arr[i + 1]]]
            elif mini_now == mini:
                res.append([arr[i], arr[i + 1]])

        return res

