# 힙을 이용한 점토 놀이 문제와 거의 같음
import heapq


n = int(input())

works = [] # 업무량 최소힙
gone_over = 0 # 검토량

for _ in range(n):
    heapq.heappush(works, int(input()))

while len(works) > 1:
    temp = heapq.heappop(works) + heapq.heappop(works) # 힙에서 제일 작은 두 업무를 빼내서 더함
    gone_over += temp # 업무가 합쳐질 때마다 검토량에 더해줌
    heapq.heappush(works, temp) # 합쳐진 업무를 다시 힙에 넣음

print(gone_over)