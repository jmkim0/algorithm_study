import sys

a, b = map(int, sys.stdin.readline().split())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

result1 = gcd(a, b)
result2 = a*b // result1

print(result1)
print(result2)