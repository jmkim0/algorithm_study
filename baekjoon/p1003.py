import sys

t = int(sys.stdin.readline())
nums = []
for _ in range(t):
    nums.append(int(sys.stdin.readline()))

max_num = max(nums)

table = [[0, 0] for _ in range(max_num+1)]
table[0][0] = 1
table[1][1] = 1

for i in range(2, max_num+1):
    table[i][0] = table[i-1][0] + table[i-2][0]
    table[i][1] = table[i-1][1] + table[i-2][1]

for num in nums:
    print(table[num][0], table[num][1])