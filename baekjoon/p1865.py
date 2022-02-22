import sys

TC = int(sys.stdin.readline())
for _ in range(TC):
    N, M, W = map(int, sys.stdin.readline().split())
    graph = [{} for _ in range(N+1)]
    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().split())
        if E not in graph[S] or graph[S][E] > T:
            graph[S][E] = T
        if S not in graph[E] or graph[E][S] > T:
            graph[E][S] = T
    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().split())
        if E not in graph[S] or graph[S][E] > -T:
            graph[S][E] = -T
    dist = [0] * (N+1)
    for _ in range(N-1):
        for u in range(1, N+1):
            for v, w in graph[u].items():
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    nc_check = False
    for u in range(1, N+1):
        for v, w in graph[u].items():
            if dist[u] + w < dist[v]:
                nc_check = True
                break
        if nc_check:
            break
    
    print("YES" if nc_check else "NO")
            