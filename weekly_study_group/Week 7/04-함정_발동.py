count = 0
# 두 줄씩 함정이 있는 위치에 손님이 있는 지 확인
for i in range(4):
    line = input()
    line2 = input()
    for j in range(0, 8, 2):
        if line[j] == 'H':
            count += 1
    for j in range(1, 8, 2):
        if line2[j] == 'H':
            count += 1
print(count)