import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [False] * (n+1)
q = deque()
count = 0

for i in range(1, n+1):
    if visited[i]:
        continue
    q.append(i)
    visited[i] = True
    count += 1
    while q:
        u = q.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)

print(count)