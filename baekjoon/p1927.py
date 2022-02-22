import sys
from heapq import heappop, heappush

n = int(sys.stdin.readline())
pq = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        print(heappop(pq) if pq else 0)
    else:
        heappush(pq, x)