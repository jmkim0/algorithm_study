import sys
from heapq import heappop, heappush

n = int(sys.stdin.readline())
pq = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if pq:
            print(-heappop(pq))
        else:
            print(0)
    else:
        heappush(pq, -x)
