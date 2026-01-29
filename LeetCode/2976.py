# O(m + n) O(1)
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = float('inf')
        dist = [[INF] * 26 for _ in range(26)]
        
        for i in range(26):
            dist[i][i] = 0
        
        for o, c, w in zip(original, changed, cost):
            u, v = ord(o) - ord('a'), ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], w)
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        total = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            u, v = ord(s) - ord('a'), ord(t) - ord('a')
            if dist[u][v] == INF:
                return -1
            total += dist[u][v]
        
        return total


# # O((n + m) log 26) O(m)
# class Solution:
#     def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
#         import heapq
        
#         INF = float('inf')
#         graph = [[] for _ in range(26)]
#         for o, c, w in zip(original, changed, cost):
#             u, v = ord(o) - ord('a'), ord(c) - ord('a')
#             graph[u].append((v, w))
        
#         def dijkstra(src):
#             dist = [INF] * 26
#             dist[src] = 0
#             pq = [(0, src)]
            
#             while pq:
#                 d, u = heapq.heappop(pq)
#                 if d > dist[u]:
#                     continue
#                 for v, w in graph[u]:
#                     if dist[u] + w < dist[v]:
#                         dist[v] = dist[u] + w
#                         heapq.heappush(pq, (dist[v], v))
            
#             return dist
        
#         all_dist = {}
#         needed_sources = set(ord(s) - ord('a') for s, t in zip(source, target) if s != t)
#         for src in needed_sources:
#             all_dist[src] = dijkstra(src)
        
#         total = 0
#         for s, t in zip(source, target):
#             if s != t:
#                 u, v = ord(s) - ord('a'), ord(t) - ord('a')
#                 if all_dist[u][v] == INF:
#                     return -1
#                 total += all_dist[u][v]
        
#         return total

