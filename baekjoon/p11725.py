import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [set() for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].add(v)
    graph[v].add(u)

visited = [0] * (N+1)
q = deque([1])
visited[1] = 1
while q:
    u = q.popleft()
    for v in graph[u]:
        if not visited[v]:
            visited[v] = u
            q.append(v)
for i in range(2, N+1):
    print(visited[i])
