import sys
from heapq import heappop, heappush

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = [{} for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    if v not in graph[u] or w < graph[u][v]:
        graph[u][v] = w
dist = [float('inf')] * (V+1)
dist[K] = 0
pq = [(0, K)]
while pq:
    d, u = heappop(pq)
    if d > dist[u]:
        continue
    for v, w in graph[u].items():
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            heappush(pq, (nd, v))

for i in range(1, V+1):
    print(dist[i] if dist[i] != float('inf') else 'INF')