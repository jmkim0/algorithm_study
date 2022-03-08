import sys


t = int(sys.stdin.readline())

for _ in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    
    if h == 1:
        print(100 + n)
    elif w == 1:
        print(n * 100 + 1)
    else:
        print(((n-1)%h+1)*100 + (n-1)//h + 1)
