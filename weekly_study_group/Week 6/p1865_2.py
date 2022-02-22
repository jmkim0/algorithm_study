# Python 3: 31780KB / 732ms

import sys
from collections import deque

TC = int(sys.stdin.readline())
for _ in range(TC):
    # 그래프의 정점, 간선을 저장 
    # 방향이 없는 간선인 도로는 2개의 방향을 가진 각각의 간선으로 나눔
    # 연결된 정점과 방향이 같은 간선이 존재하는 경우 가중치가 작은 것만 남김
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

    # 거리를 구하는 목적이 아니라 negative cycle의 존재만을 찾으면 됨
    # 모든 정점을 0초만에 도달할 수 있는 가상의 정점이 존재하고 --
    # 이 정점에 대해 1회 미리 루프했다고 가정하여 dist를 0으로 초기화
    # 총 정점 개수, 루프수 모두 N+1회라고 봐도 무방
    dist = [0] * (N+1)

    # SPFA를 위한 queue
    # 위 dist와 같은 이유로 q에 미리 1부터 N까지의 정점이 들어가게 됨
    q = deque(range(1, N+1))

    # q membership check를 빠르게 하기 위한 flag 배열
    in_queue = [True] * (N+1)

    # negative cycle 검출을 위한 최소경로가 지나는 간선 수 배열
    # 어떤 경로에서 지나는 간선 수가 정점의 수와 같으면 무조건 cycle이 존재함
    # 최소경로를 구하는 알고리즘 상에서의 cycle은 negative cycle을 의미함
    edge_count = [0] * (N+1)
    nc_check = False # negative cycle check flag

    # SPFA
    while q:
        u = q.popleft()
        in_queue[u] = False
        for v, w in graph[u].items():
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                edge_count[v] = edge_count[u] + 1
                if edge_count[v] == N:
                    nc_check = True
                    break                
                if not in_queue[v]:
                    q.append(v)
                    in_queue[v] = True
        if nc_check:
            break
    
    print("YES" if nc_check else "NO")