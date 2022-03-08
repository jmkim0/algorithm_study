import sys
from collections import deque


n = int(sys.stdin.readline())
dq = deque()

for _ in range(n):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == 'push_back':
        dq.append(int(cmd[1]))

    elif cmd[0] == 'push_front':
        dq.appendleft(int(cmd[1]))

    elif cmd[0] == 'size':
        print(len(dq))

    elif cmd[0] == 'empty':
        print(0 if dq else 1)

    elif cmd[0] == 'front':
        print(dq[0] if dq else -1)

    elif cmd[0] == 'back':
        print(dq[-1] if dq else -1)
    
    elif cmd[0] == 'pop_front':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif cmd[0] == 'pop_back':
        if dq:
            print(dq.pop())
        else:
            print(-1)