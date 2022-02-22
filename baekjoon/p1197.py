import sys

def find(a):
    if parents[a] == a:
        return a
    parents[a] = find(parents[a]) # 이 부분이 중요!! memoization
    return parents[a]

V, E = map(int, sys.stdin.readline().split())
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(E)]
parents = [i for i in range(V+1)]
edges.sort(key=lambda x: x[2])
result = 0
for u, v, w in edges:
    pu = find(u)
    pv = find(v) 
    if pu != pv:
        parents[pv] = pu
        result += w
print(result)