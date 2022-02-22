import sys

n = int(sys.stdin.readline())
p_list = list(map(int, sys.stdin.readline().split()))

table = [0] * n

for i in range(n):
    table[i] = p_list[i]
    for j in range(i):
        temp = p_list[j] + table[i-j-1]
        if table[i] < temp:
            table[i] = temp

print(table[n-1])