import sys

n = int(sys.stdin.readline())
rgb = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

table = [[0]*3 for _ in range(n)]
table[0] = rgb[0]
for i in range(1, n):
    table[i][0] = rgb[i][0] + min(table[i-1][1], table[i-1][2])
    table[i][1] = rgb[i][1] + min(table[i-1][0], table[i-1][2])
    table[i][2] = rgb[i][2] + min(table[i-1][1], table[i-1][0])
print(min(table[n-1]))