from math import comb

n, m = map(int, input().split())

# print(comb(n, m))

k = m
if k*2 > n:
    k = n - k

result = 1
for i in range(n, n-k, -1):
    result *= i
for i in range(2, k+1):
    result //= i

print(result)