N = int(input())
C = tuple(map(int, input().split()))
M = int(input())

# 모든 조합 하나씩 구하기
# m = [set() for _ in range(M + 1)]
# m[0].add(tuple([0 for _ in range(N)]))
# for i in range(1, M+1):
#     for j in range(N):
#         if C[j] <= i:
#             for seq in m[i-C[j]]:
#                 new_seq = list(seq)
#                 new_seq[j] += 1
#                 m[i].add(tuple(new_seq))
# print(len(m[M]))

# DP 1
m = [[0] * N for _ in range(M+1)]
m[0] = [1] * N
for i in range(1, M+1):
    m[i][0] = 1 if i % C[0] == 0 else 0
    for j in range(1, N):
        m[i][j] = m[i][j-1]
        if C[j] <= i:
            # for k in range(C[j], i + 1, C[j]):
            #     m[i][j] += m[i-k][j-1]
            m[i][j] += m[i-C[j]][j]
print(m[M][N-1])

# DP 2
# m = [0] * (M+1)
# m[0] = 1
# for c in C:
#     for j in range(c, M + 1):
#         m[j] += m[j-c]
        
# print(m[M])