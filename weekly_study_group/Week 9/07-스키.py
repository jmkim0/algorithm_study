import sys

N, M = map(int, sys.stdin.readline().split())
data = []
for _ in range(N):
    data.append(tuple(map(int, sys.stdin.readline().split())))
dp = [[0] * M for _ in range(N)]
dp[0][0] = data[0][0]
for j in range(1, M):
    dp[0][j] = dp[0][j-1] + data[0][j]
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + data[i][0]
    for j in range(1, M):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + data[i][j]
print(dp[N-1][M-1])