from heapq import heappush, heappop

N, K = map(int, input().split())
T = [int(input()) for _ in range(N)]
pq = []
uptime = T[N-1]+1 - T[0]
for i in range(N-1):
    heappush(pq, T[i]+1 - T[i+1])

for _ in range(K-1):
    uptime += heappop(pq)

print(uptime)