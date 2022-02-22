import sys
from collections import deque

while True:
    line = sys.stdin.readline()
    if line.isspace():
        continue
    else:
        L, R, C = map(int, line.split())
    if L == 0 and R == 0 and C == 0:
        break
    graph = []
    start = None
    end = None
    for l in range(L):
        graph.append([])
        for r in range(R):
            row = sys.stdin.readline().strip()
            graph[l].append(row)
            if not start:
                c = row.find('S')
                if c != -1:
                    start = (l, r, c)
            if not end:
                c = row.find('E')
                if c != -1:
                    end = (l, r, c)
        if l < L-1:
            sys.stdin.readline()
            
    if not end:
        print("탈출 불가")
    else:
        q = deque([start])
        visited = [[[-1] * C for _ in range(R)] for _ in range(L)]
        l, r, c = start
        visited[l][r][c] = 0
        while q:
            l, r, c = q.popleft()
            for dl, dr, dc in (0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0):
                nl = l + dl
                nr = r + dr
                nc = c + dc
                if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C and visited[nl][nr][nc] == -1 and graph[nl][nr][nc] != '#':
                    visited[nl][nr][nc] = visited[l][r][c] + 1
                    q.append((nl, nr, nc))
        l, r, c = end
        result = visited[l][r][c]
        if result == -1:
            print("탈출 불가")
        else:
            print(f"탈출 성공 : {result}분")