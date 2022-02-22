n = int(input())
n_list = input().split(" ")
for i in range(n):
    n_list[i] = int(n_list[i])
print(min(n_list), max(n_list))