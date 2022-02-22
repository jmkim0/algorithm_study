import sys

N, M = map(int, sys.stdin.readline().split())
matrix = [[0]*(N+1)] + [[0]+list(map(int, sys.stdin.readline().split())) for _ in range(N)]
table = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        table[i][j] = matrix[i][j] + table[i-1][j] + table[i][j-1] - table[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(table[x2][y2] - table[x1-1][y2] - table[x2][y1-1] + table[x1-1][y1-1])