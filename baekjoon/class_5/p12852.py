from collections import deque

N = int(input())
visited = [None] * (N+1)
visited[1] = [1]
q = deque([1])

while q:
    x = q.popleft()
    if x == N:
        print(len(visited[N])-1)
        print(*visited[N])
        break
    if x+1 <= N and not visited[x+1]:
        visited[x+1] = [x+1] + visited[x]
        q.append(x+1)
    if x*2 <= N and not visited[x*2]:
        visited[x*2] = [x*2] + visited[x]
        q.append(x*2)
    if x*3 <= N and not visited[x*3]:
        visited[x*3] = [x*3] + visited[x]
        q.append(x*3)
