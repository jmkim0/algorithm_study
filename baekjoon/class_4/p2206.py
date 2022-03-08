import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
matrix = tuple(sys.stdin.readline().strip() for _ in range(N))
visited = [[[-1]*2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
q = deque([(0, 0, 0)])
while q:
    y, x, breaked = q.popleft()
    for dy, dx in (1, 0), (0, 1), (-1, 0), (0, -1):
        ny = y + dy
        nx = x + dx
        if 0<=ny<N and 0<=nx<M:
            if matrix[ny][nx] == '1' and not breaked and visited[ny][nx][1] == -1:
                visited[ny][nx][1] = visited[y][x][0] + 1
                q.append((ny, nx, 1))
            elif matrix[ny][nx] == '0' and visited[ny][nx][breaked] == -1:
                visited[ny][nx][breaked] = visited[y][x][breaked] + 1
                q.append((ny, nx, breaked))
if visited[N-1][M-1] == -1 and visited[N-1][M-1][1] == -1:
    print('-1')
elif visited[N-1][M-1][0] == -1:
    print(visited[N-1][M-1][1])
elif visited[N-1][M-1][1] == -1:
    print(visited[N-1][M-1][0])
else:
    print(min(visited[N-1][M-1]))
