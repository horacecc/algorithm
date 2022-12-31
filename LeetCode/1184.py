# O(n) O(1)
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total = sum(distance)
        d = 0
        if start > destination:
            start, destination = destination, start
        for i in range(start, destination):
            d += distance[i]
        return min(d, total - d)
