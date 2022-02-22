t = int(input())
r_list = []
s_list = []
for i in range(t):
    r_s = input().split(' ')
    r_list.append(int(r_s[0]))
    s_list.append(r_s[1])

for i in range(t):
    p = ''
    for char in s_list[i]:
        p += char * r_list[i]
    print(p)
