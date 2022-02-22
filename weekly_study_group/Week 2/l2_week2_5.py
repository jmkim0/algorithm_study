n = int(input())
# 매움 수치를 리스트로 받음
pungency_list = list(map(int, input().split()))

powder1 = 0
powder2 = 0
# 모든 가루 조합에 대해서 계산함 (i번째 가루 + j번째 가루)
# 0 <= i <= n-1 / i+1 <= j <= n
for i in range(n-1):
    for j in range(i+1, n):
        if j == 1:
            powder1 = pungency_list[0]
            powder2 = pungency_list[1]
        elif abs(powder1 + powder2) > abs(pungency_list[i] + pungency_list[j]):
            powder1 = pungency_list[i]
            powder2 = pungency_list[j]
        elif abs(powder1 + powder2) == abs(pungency_list[i] + pungency_list[j]):
            if abs(powder1)+abs(powder2) < abs(pungency_list[i])+abs(pungency_list[j]):
                powder1 = pungency_list[i]
                powder2 = pungency_list[j]

print(powder1, powder2)