import sys

N = int(sys.stdin.readline())
result = 0
x1, y1 = map(int, sys.stdin.readline().split())
x, y = x1, y1
for _ in range(N-1):
    nx, ny = map(int, sys.stdin.readline().split())
    result += x*ny - nx*y
    x, y = nx, ny
result += x*y1 - x1*y
result = abs(result) / 2
print(f"{result:.1f}")