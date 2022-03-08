import sys


n = int(sys.stdin.readline())
s = []

for _ in range(n):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == 'push':
       s.append(int(cmd[1]))

    elif cmd[0] == 'size':
        print(len(s))

    elif cmd[0] == 'empty':
        print(0 if s else 1)

    elif cmd[0] == 'top':
        print(s[-1] if s else -1)
    
    elif cmd[0] == 'pop':
        if s:
            print(s.pop())
        else:
            print(-1)