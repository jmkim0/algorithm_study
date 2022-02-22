min_bottle = int(input())

for _ in range(2):
    bottle = int(input())
    if bottle < min_bottle:
        min_bottle = bottle

min_cap = int(input())

cap = int(input())

if cap < min_cap:
    min_cap = cap
    
print(min_bottle + min_cap + 10)
        
    
