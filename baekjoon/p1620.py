import sys

n, m = map(int, sys.stdin.readline().split())
num2name = {}
name2num = {}
for i in range(1, n+1):
    name = sys.stdin.readline().strip()
    num2name[str(i)] = name
    name2num[name] = i

for _ in range(m):
    q = sys.stdin.readline().strip()
    if q in num2name:
        print(num2name[q])
    else:
        print(name2num[q])