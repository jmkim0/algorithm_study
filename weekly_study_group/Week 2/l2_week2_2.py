n = int(input())

n = 10000 - n
n, count = n % 1000, n // 1000
n, count = n % 100, count + n//100
n, count = n % 10, count + n//10
count += n

print(count)