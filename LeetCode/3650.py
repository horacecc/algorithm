import heapq

# O((n + m) log n) O(n + m)
# m = len(edges)
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w * 2))
        
        dist = [float('inf')] * n
        dist[0] = 0
        pq = [(0, 0)]

        while pq:
            d, u = heapq.heappop(pq)
            
            if d > dist[u]:
                continue
            
            if u == n - 1:
                return d
            
            for v, w in graph[u]:
                new_dist = d + w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))

        return -1

