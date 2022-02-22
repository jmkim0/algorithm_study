from heapq import heappush, heappop

N, M = map(int, input().split())
vms = tuple(map(int, input().split()))
free = []
in_use = []
t = 0
for i in range(M):
    heappush(free, i)
for _ in range(N):
    if not free:
        t = in_use[0][0]
        while in_use and in_use[0][0] == t:
            t_, n_ = heappop(in_use)
            heappush(free, n_)
    n = heappop(free)
    heappush(in_use, (t + vms[n], n))
print(n+1)