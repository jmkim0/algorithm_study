M = int(input())
num = '1'
for _ in range(M):
    X, Y = input().split()
    if X == num:
        num = Y
    elif Y == num:
        num = X
print(num)