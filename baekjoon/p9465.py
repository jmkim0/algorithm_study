import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())

    if n == 1:
        data = [int(sys.stdin.readline()), int(sys.stdin.readline())]
        print(max(data))
        continue

    data = [list(map(int, sys.stdin.readline().split())), 
            list(map(int, sys.stdin.readline().split()))]
    table = [[0]*n, [0]*n]
    table[0][0] = data[0][0]
    table[1][0] = data[1][0]
    table[0][1] = table[1][0] + data[0][1]
    table[1][1] = table[0][0] + data[1][1]
    for i in range(2, n):
        table[0][i] = max(table[0][i-2], table[1][i-2], table[1][i-1]) + data[0][i]
        table[1][i] = max(table[0][i-2], table[1][i-2], table[0][i-1]) + data[1][i]
    print(max(table[0][-2], table[0][-1], table[1][-2], table[1][-1]))
    