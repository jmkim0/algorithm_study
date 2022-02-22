r, c, k = map(int, input().split(' '))

# 1회 여행은 무조건 가능
if k == 1:
    print(1)
# 2회 이상의 경우
# 1) (1, 2), (2, 1) 일 때 가능 -> r이 1일 때 c>2면 불가능, c가 1일때 r>2면 불가능
# 2) r, c >= 2에서 r, c 중 하나가 짝수이면 가능 -> r, c 가 둘 다 홀수이면 불가능
# 조건을 적당히 짧게 쓰는 방법으로 바꿔서 씀
elif (r%2 and c%2) or (r==1 and c>2) or (c==1 and r>2):
    print(0)
else:
    print(1)
    