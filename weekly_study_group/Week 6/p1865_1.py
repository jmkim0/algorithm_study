# Python 3: 29452KB / 2712ms

import sys

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

    # 벨만-포드 알고리즘에서와 같이 N-1회 루프
    for _ in range(N-1):
        for u in range(1, N+1):
            for v, w in graph[u].items():
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    
    nc_check = False # negative cycle check flag
    # negative cycle을 탐지하기 위한 마지막 루프
    for u in range(1, N+1):
        for v, w in graph[u].items():
            if dist[u] + w < dist[v]:
                nc_check = True
                break
        if nc_check:
            break
    
    print("YES" if nc_check else "NO")