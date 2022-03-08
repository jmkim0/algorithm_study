from collections import deque

n, k = map(int, input().split())

visited = [0] * 100001
visited[n] = 0
q = deque([n])

while q:
    x = q.popleft()
    t = visited[x]
    if x == k:
        print(t)
        break
    if 0 <= x-1 and not visited[x-1]:
        visited[x-1] = t+1
        q.append(x-1)
    if x+1 <= 100000 and not visited[x+1]:
        visited[x+1] = t+1
        q.append(x+1)
    if 2*x <= 100000 and not visited[2*x]:
        visited[2*x] = t+1
        q.append(2*x)
