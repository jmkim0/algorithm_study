import heapq
import sys

MAX_OP = 1000000

result = []
t = int(sys.stdin.readline())

for _ in range(t):
    max_heap = []
    min_heap = []
    popped = [False] * MAX_OP

    k = int(sys.stdin.readline())
    
    for i in range(k):
        op, num = sys.stdin.readline().split()

        if op == 'I':
            heapq.heappush(max_heap, (-int(num), i))
            heapq.heappush(min_heap, (int(num), i))
        
        elif op == 'D':
            if num == '1':
                while max_heap:
                    temp = heapq.heappop(max_heap)[1]
                    if popped[temp]:
                        continue
                    else:
                        popped[temp] = True
                        break

            elif num == '-1':
                while min_heap:
                    temp = heapq.heappop(min_heap)[1]
                    if popped[temp]:
                        continue
                    else:
                        popped[temp] = True
                        break

    while max_heap and popped[max_heap[0][1]]:
        heapq.heappop(max_heap)

    while min_heap and popped[min_heap[0][1]]:
        heapq.heappop(min_heap)


    if max_heap and min_heap:
        result.append(f'{-max_heap[0][0]} {min_heap[0][0]}')
    else:
        result.append('EMPTY')

for line in result:
    print(line)
