import sys

num_list = []

while True:
    temp = sys.stdin.readline().strip()
    
    if temp == '0':
        break
    
    num_list.append(temp)

def is_pelindrome(num):
    n = len(num)

    if n == 1:
        return 'yes'
    
    for i in range(n//2):
        if num[i] != num[-1-i]:
            return 'no'
    
    return 'yes'

for num in num_list:
    print(is_pelindrome(num))
