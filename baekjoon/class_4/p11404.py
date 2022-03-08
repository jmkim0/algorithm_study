import sys
from heapq import heappop, heappush

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [{} for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    if v not in graph[u] or w < graph[u][v]:
        graph[u][v] = w
dist = [[float('inf')]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dist[i][i] = 0
    pq = [(0, i)]
    while pq:
        d, u = heappop(pq)
        if d > dist[i][u]:
            continue
        for v, w in graph[u].items():
            nd = d + w
            if nd < dist[i][v]:
                dist[i][v] = nd
                heappush(pq, (nd, v))
for i in range(1, n+1):
    for j in range(1, n):
        print(dist[i][j] if dist[i][j] != float('inf') else 0, end=' ')
    print(dist[i][n] if dist[i][n] != float('inf') else 0)