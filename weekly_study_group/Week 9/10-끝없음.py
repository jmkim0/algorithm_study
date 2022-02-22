import sys
sys.setrecursionlimit(10**6)

s = input()
S = input()
count = int(input())
min_, max_ = map(int, input().split())

def make_str(s, S, count, max_):
    ns = ''
    for c in S:
        if c == '$':
            ns += s
        else:
            ns += c
    if count == 1 or len(ns) >= max_:
        return ns
    else:
        return make_str(ns, S, count - 1, max_)

ns = make_str(s, S, count, max_)
ns += '-' * (max_ - len(ns))
print(ns[min_-1:max_])