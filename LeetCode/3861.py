class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        res = -1

        for i in range(len(capacity)):
            if capacity[i] >= itemSize:
                if res == -1 or capacity[res] > capacity[i]:
                    res = i

        return res
