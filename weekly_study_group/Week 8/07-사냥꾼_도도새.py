N = int(input())
H = tuple(map(int, input().split()))

m = [[] for _ in range(N)]
m[0] = [H[0]-1]
for i in range(1, N):
    m[i] = m[i-1]
    if H[i] in m[i]:
        m[i][m[i].index(H[i])] -= 1
    else:
        m[i].append(H[i] - 1)
print(len(m[N-1]))