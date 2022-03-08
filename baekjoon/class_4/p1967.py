import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [{} for _ in range(n+1)]
for _ in range(n-1):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u][v] = w
    graph[v][u] = w
visited = [-1] * (n+1)
visited[1] = 0
q = deque([1])
while q:
    u = q.popleft()
    for v, w in graph[u].items():
        if visited[v] == -1:
            visited[v] = visited[u] + w
            q.append(v)
start = 0
max_len = 0
for i in range(1, n+1):
    if visited[i] > max_len:
        start = i
        max_len = visited[i]
visited = [-1]*(n+1)
visited[start] = 0
q = deque([start])
while q:
    u = q.popleft()
    for v, w in graph[u].items():
        if visited[v] == -1:
            visited[v] = visited[u] + w
            q.append(v)
print(max(visited))