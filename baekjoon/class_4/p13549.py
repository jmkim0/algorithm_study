from collections import deque

N, K = map(int, input().split())

visited = [-1] * 100001
visited[N] = 0
q = deque([N])

while q:
    x = q.popleft()
    t = visited[x]
    if x == K:
        print(t)
        break
    xt = x * 2
    while 0 < xt < 100001:
        if visited[xt] == -1 or visited[xt] > t:
            visited[xt] = t
            q.appendleft(xt)
        xt *= 2
    if 0 <= x-1 and visited[x-1] == -1:
        visited[x-1] = t+1
        q.append(x-1)
    if x+1 <= 100000 and visited[x+1] == -1:
        visited[x+1] = t+1
        q.append(x+1) 