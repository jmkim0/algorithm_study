t = int(input())
max_num = 0
nums = []
for _ in range(t):
    n = int(input())
    if n > max_num:
        max_num = n
    nums.append(n)

table = [1] * (max_num+1)
if max_num >= 2:
    table[2] = 2
    if max_num >= 3:
        for i in range(3, max_num+1):
            table[i] = table[i-1] + table[i-2] + table[i-3]

for num in nums:
    print(table[num])
