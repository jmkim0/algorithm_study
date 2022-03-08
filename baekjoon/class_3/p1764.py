import sys

n, m = map(int, sys.stdin.readline().split())
unheard = set()
uhus = []

for _ in range(n):
    unheard.add(sys.stdin.readline().strip())

for _ in range(m):
    name = sys.stdin.readline().strip()
    if name in unheard:
        uhus.append(name)

uhus.sort()

print(len(uhus))
for name in uhus:
    print(name)
