import sys

n = int(sys.stdin.readline())
a_iter = map(int, sys.stdin.readline().split())
a_dict = {}

for num in a_iter:
    a_dict[num] = 1

m = int(sys.stdin.readline())
m_iter = map(int, sys.stdin.readline().split())

for num in m_iter:
    if num in a_dict:
        print(1)
    else:
        print(0)
