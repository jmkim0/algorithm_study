import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
visited[1] = True
count = 0
q = deque([1])

while q:
    node = q.popleft()

    for next in graph[node]:
        if not visited[next]:
            visited[next] = True
            count += 1
            q.append(next)

print(count)