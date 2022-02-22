import sys


n, k = map(int, sys.stdin.readline().split())
num_str = sys.stdin.readline()

result = ''
start = 0
num_len = n-k

while k > 0 and len(result) < num_len:
    max_digit = num_str[start]
    max_index = start

    for i in range(start, start+k+1):
        if max_digit < num_str[i]:
            max_digit = num_str[i]
            max_index = i

        if max_digit == '9':
            break

    result += max_digit
    k -= (max_index - start)
    start = max_index + 1

if k == 0:
    result += num_str[start:]

print(result)