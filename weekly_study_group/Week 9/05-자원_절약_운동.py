import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [set() for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].add(b)
    graph[b].add(a)
# 단계가 최대인 경우는 일렬로 20노드가 있을 때: 20*19/2 = 190
# 적당히 200으로 최소 단계수의 초기값을 정함
min_steps = 200 
min_node = 0
for i in range(1, N+1):
    q = deque([i])
    visited = [0] * (N+1)
    while q:
        a = q.popleft()
        for b in graph[a]:
            if b != i and visited[b] == 0:
                visited[b] = visited[a] + 1
                q.append(b)
    steps = sum(visited)
    if steps < min_steps:
        min_steps = steps
        min_node = i
print(min_node)