n = int(input())

table = [0] * (n+1)
table[1] = 0

for i in range(2, n+1):
    table[i] = min(table[i-1]+1, table[i//2]+i%2+1, table[i//3]+i%3+1)

print(table[n])