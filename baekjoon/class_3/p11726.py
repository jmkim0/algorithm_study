n = int(input())

table = [1] * (n+1)
for i in range(2, n+1):
    table[i] = (table[i-1] + table[i-2]) % 10007

print(table[n])