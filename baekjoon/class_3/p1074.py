import sys

def z_nth(n, r, c):
    if n == 1:
        return 2*r + c
    mul = 0
    nr, nc = r, c
    half = 2**(n-1)
    if r >= half:
        mul += 2
        nr -= half
    if c >= half:
        mul += 1
        nc -= half
    return mul*half**2 + z_nth(n-1, nr, nc)

n, r, c = map(int, sys.stdin.readline().split())
print(z_nth(n, r, c))
