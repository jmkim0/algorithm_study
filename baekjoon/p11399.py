n = int(input())
p_list = sorted(map(int, input().split()))
result = 0
for i in range(1, n+1):
    result += i * p_list[-i]
print(result)
