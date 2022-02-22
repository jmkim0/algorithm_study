import sys
from collections import deque
# sys.setrecursionlimit(2502)

# def dfs(matrix, y, x, visited):
#     n = len(matrix)
#     m = len(matrix[0])
#     visited[y][x] = True

#     for dy, dx in (1, 0), (0, 1), (-1, 0), (0, -1):
#         ny = y + dy
#         nx = x + dx
#         if 0 <= ny < n and 0 <= nx < m and matrix[ny][nx] == 1 and not visited[ny][nx]:
#             dfs(matrix, ny, nx, visited)

# main
t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    matrix = [[0]*m for _ in range(n)]
    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        matrix[y][x] = 1
    count = 0
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and not visited[i][j]:
                count += 1
                q = deque([(i, j)])
                visited[i][j] = True
                while q:
                    y, x = q.popleft()
                    
                    for dy, dx in (1, 0), (0, 1), (-1, 0), (0, -1):
                        ny = y + dy
                        nx = x + dx
                        if 0 <= ny < n and 0 <= nx < m and matrix[ny][nx] == 1 and not visited[ny][nx]:
                            visited[ny][nx] = True # q에 넣기 전에 visited 체크해줘야 중복이 없음
                            q.append((ny, nx))
                # dfs(matrix, y, x, visited)

    print(count)
    