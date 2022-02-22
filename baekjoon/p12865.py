import sys

N, K = map(int, sys.stdin.readline().split())
items = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(N)])
table = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        w, v = items[i-1]
        if j >= w:
            table[i][j] = max(v+table[i-1][j-w], table[i-1][j])
        else:
            table[i][j] = table[i-1][j]
            
print(table[N][K])