max_value = 0
max_nth = 0
for i in range(9):
    n = int(input())
    if n > max_value:
        max_nth = i + 1
        max_value = n
print(max_value)
print(max_nth)