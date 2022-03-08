n = int(input())
result = []

for i in range(n):
    a_b = input().split(" ")
    result.append(int(a_b[0]) + int(a_b[1]))

for i in range(n):
    print(result[i])