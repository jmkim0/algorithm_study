import sys


def is_vps(ps):
    s = []

    for p in ps:
        if p == '(':
            s.append(p)
        elif s and s[-1] == '(':
            s.pop()
        else:
            return False
    
    return False if s else True


t = int(sys.stdin.readline())

for _ in range(t):
    if is_vps(sys.stdin.readline().strip()):
        print('YES')
    else:
        print('NO')