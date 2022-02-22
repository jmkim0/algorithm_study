# 요세푸스 순열과 거의 같다. 근데 이제 deque를 곁들인

from collections import deque

n, k, m = map(int, input().split())

count = 0 # 숫자를 뺀 횟수

q = deque(range(1, n+1))

while q:
    q.rotate(-k+1) # 왼쪽으로 k-1만큼 회전 ex) 1, ..., k, ..., n -> k, ..., n, 1, ..., k-1
    num = q.popleft() # 맨 왼쪽 숫자를 빼냄, 즉 k번째 숫자가 빠짐
    count += 1 # 숫자를 뺀 횟수를 셈
    if num == m: # 그 숫자가 m이면 루프를 종료함
        break

print(count)