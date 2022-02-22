# [0826] 실시간 문제풀이 특강 참조
import heapq

n, t, p = map(int, input().split())
coals = list(map(int, input().split()))

time = 0
answer = 0
mining = []

for c in coals:
    heapq.heappush(mining, -c)
    time = time + c
    
    if time > t:
        time = time + heapq.heappop(mining)
        
    answer = max(len(mining), answer)
    time = time + p
    
print(answer)