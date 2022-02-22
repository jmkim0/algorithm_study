N, T = map(int, input().split())
orders = map(int, input().split())

count = 0
time_passed = 0

# 주문을 시간이 초과될 때까지 하나씩 받아봄
for order in orders:
    time_passed += order
    if time_passed <= T:
        count += 1
    else:
        break

print(count)