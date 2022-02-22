import sys
from heapq import heappop, heappush


n = int(sys.stdin.readline())
pq = []

for i in range(n):
    age, name = sys.stdin.readline().split()
    
    heappush(pq, (int(age), i, name))

for _ in range(n):
    age, i, name = heappop(pq)

    print(age, name)