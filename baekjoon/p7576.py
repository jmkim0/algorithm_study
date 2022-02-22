import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            q.append((i, j))

while q:
    y, x = q.popleft()

    for dy, dx in (1, 0), (0, 1), (-1, 0), (0, -1):
        ny = y + dy
        nx = x + dx
        if 0 <= ny < n and 0 <= nx < m and matrix[ny][nx] == 0:
            matrix[ny][nx] = matrix[y][x] + 1
            q.append((ny, nx))

result = 1
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            result = 0
            break
        if matrix[i][j] > result:
            result = matrix[i][j]
    if result == 0:
        break

print(result-1)
        