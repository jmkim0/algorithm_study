T = int(input())
N = int(input())
A = tuple(map(int, input().split()))
M = int(input())
B = tuple(map(int, input().split()))

# A에서 나올 수 있는 합들을 dict에 저장 - O(N^2)
# key: 부분합의 값, value: 부분합을 만드는 경우의 수
sum_A_dict = {}
for i in range(N):
    sum_A = 0
    for j in range(i, N):
        sum_A += A[j]
        if sum_A in sum_A_dict:
            sum_A_dict[sum_A] += 1
        else:
            sum_A_dict[sum_A] = 1

# B의 부분합과 A의 부분합을 합했을 때 T가 되는 경우를 T - (B의 부분합)이  
# 위에서 만든 A의 부분합 dict안에 있는지를 확인하는 방법으로 셈 - O(M^2)
sum_B_dict = {}
count = 0
for i in range(M):
    target = T
    for j in range(i, M):
        target -= B[j]
        if target in sum_A_dict:
            count += sum_A_dict[target]

print(count)