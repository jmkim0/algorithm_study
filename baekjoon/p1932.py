import sys

n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
table = [[0]*i for i in range(1, n+1)]
table[0][0] = data[0][0]
for i in range(1, n):
    table[i][0] = data[i][0] + table[i-1][0]
    table[i][-1] = data[i][-1] + table[i-1][-1]
    for j in range(1, i):
        table[i][j] = data[i][j] + max(table[i-1][j], table[i-1][j-1])
print(max(table[n-1]))