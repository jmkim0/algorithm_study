import sys
from heapq import heappop, heappush


n = int(sys.stdin.readline())
points = []

for _ in range(n):
    heappush(points, tuple(map(int, sys.stdin.readline().split())))

for _ in range(n):
    print(*heappop(points))