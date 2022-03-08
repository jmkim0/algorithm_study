import sys

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

max_sum = 0

cards.sort()

for i in range(n-2):
    if i > 1 and cards[i] == cards[i-1]:
        continue
    
    for j in range(i+1, n-1):
        if j > i+1 and cards[j] == cards[j-1]:
            continue
        
        for k in range(j+1, n):
            if k > j+1 and cards[k] == cards[k-1]:
                continue

            temp = cards[i] + cards[j] + cards[k]

            if max_sum < temp < m:
                max_sum = temp
            elif temp == m:
                max_sum = m
                break
            elif temp > m:
                break
        
        if max_sum == m:
            break
    
    if max_sum == m:
        break

print(max_sum)

