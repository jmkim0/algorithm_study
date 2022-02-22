import sys
sys.setrecursionlimit(10**9)

def dfs(graph, start, cur, visited):
    for next in iter(graph[cur]):
        if next != start and visited[next] == 0:
            visited[next] = visited[cur] + graph[cur][next]
            dfs(graph, start, next, visited)

v = int(sys.stdin.readline())
graph = [{} for _ in range(v+1)]
for _ in range(v):
    edges = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(edges)-1, 2):
        graph[edges[0]][edges[j]] = edges[j+1]
visited = [0]*(v+1)
dfs(graph, 1, 1, visited)
start = 0
max_len = 0
for i in range(1, v+1):
    if visited[i] > max_len:
        start = i
        max_len = visited[i]
visited = [0]*(v+1)
dfs(graph, start, start, visited)
print(max(visited))