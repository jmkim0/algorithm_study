import sys

m = int(sys.stdin.readline())
s = [0] * 21
for _ in range(m):
    op = sys.stdin.readline().split()
    if op[0] == 'add':
        s[int(op[1])] = 1
    if op[0] == 'remove':
        s[int(op[1])] = 0
    if op[0] == 'check':
        print(s[int(op[1])])
    if op[0] == 'toggle':
        s[int(op[1])] ^= 1
    if op[0] == 'all':
        s = [1] * 21
    if op[0] == 'empty':
        s = [0] * 21