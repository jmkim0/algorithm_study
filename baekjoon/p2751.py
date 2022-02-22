import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
pq = []

for _ in range(n):
    heappush(pq, sys.stdin.readline())

result = ''
for _ in range(n):
    result += heappop(pq)

print(result)