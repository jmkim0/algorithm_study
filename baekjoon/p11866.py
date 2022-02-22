import sys
from collections import deque


n, k = map(int, sys.stdin.readline().split())
dq = deque(range(1, n+1))
result = '<'

for i in range(n-1):
    dq.rotate(-k+1)
    result += str(dq.popleft())
    result += ', '
    
result += str(dq.popleft())
result += '>'

print(result)