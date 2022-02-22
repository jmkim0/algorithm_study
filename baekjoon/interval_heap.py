# depq(double-ended priority queue)
# interval heap 이용 (https://www.cise.ufl.edu/~sahni/dsaaj/enrich/c13/double.htm)
# list로 구현
# depq[2*i:2*(i+1)]: i번 노드의 interval ex) 0번 노드의 interval: [depq[0], depq[1]]
# i번 노드의 자식: (2*i + 1)번, (2*i + 2)번 -> i번 노드의 부모: ((i-1) >> 1)번
import sys


def depq_push(depq, elem):
    n = len(depq)
    
    if n == 0:
        depq.append(elem)
    
    elif n == 1:
        if depq[0] <= elem:
            depq.append(elem)
        else:
            depq.insert(0, elem)

    elif n%2 == 0:
        depq.append(elem)

        cur = ((n>>1) - 1) >> 1
        left = cur << 1
        right = left + 1

        if depq[left] > elem:
            depq[-1] = depq[left]
            depq[left] = elem
            
            while cur > 0:
                nxt = (cur-1) >> 1
                nxt_left = nxt << 1

                if depq[nxt_left] > elem:
                    depq[left] = depq[nxt_left]
                    depq[nxt_left] = elem
                    cur = nxt
                else:
                    return
        
        elif depq[right] < elem:
            depq[-1] = depq[right]
            depq[right] = elem

            while cur > 0:
                nxt = (cur-1) >> 1
                nxt_right = (nxt << 1) + 1
                if depq[nxt_right] < elem:
                    depq[right] = depq[nxt_right]
                    depq[nxt_right] = elem
                    cur = nxt
                else:
                    return
            
    else:
        if depq[-1] <= elem:
            depq.append(elem)

            cur = ((n>>1) - 1) >> 1
            right = (cur << 1) + 1

            if depq[right] < elem:
                depq[-1] = depq[right]
                depq[right] = elem

                while cur > 0:
                    nxt = (cur-1) >> 1
                    nxt_right = (nxt << 1) + 1

                    if depq[nxt_right] < elem:
                        depq[right] = depq[nxt_right]
                        depq[nxt_right] = elem
                        cur = nxt
                    else:
                        return

        else:
            temp = depq[-1]
            depq.append(temp)
            depq[-2] = elem

                
            cur = (n-2) >> 1
            left = cur << 1

            if depq[left] > elem:
                depq[-2] = depq[left]
                depq[left] = elem

                while cur > 0:
                    nxt = (cur-1) >> 1
                    nxt_left = nxt << 1
                    if depq[nxt_left] > elem:
                        depq[left] = depq[nxt_left]
                        depq[nxt_left] = elem
                        cur = nxt
                    else:
                        return


def depq_pop_min(depq):
    n = len(depq)
    
    if n == 0:
        raise IndexError

    elif n <= 2:
        return depq.pop(0)

    result = depq[0]
    
    if n%2 == 1:
        depq[0] = depq.pop()

    else:
        depq[0] = depq[-2]
        depq[-2] = depq[-1]
        depq.pop()
    
    n -= 1
    cur = 0
    limit = (n-1) >> 1

    while cur < limit:
        left = (cur<<1) + 1
        right = left + 1
        min_node = cur

        if (left<<1) < n and depq[left<<1] < depq[min_node<<1]:
            min_node = left
        
        if (right<<1) < n and depq[right<<1] < depq[min_node<<1]:
            min_node = right
        
        if min_node != cur:
            min_index = min_node << 1
            temp = depq[min_index]
            depq[min_index] = depq[cur<<1]
            depq[cur<<1] = temp
            
            if min_index+1 < n and depq[min_index] > depq[min_index+1]:
                temp = depq[min_index]
                depq[min_index] = depq[min_index+1]
                depq[min_index+1] = temp
            
            cur = min_node
        
        else:
            break

    return result
    

def depq_pop_max(depq):
    n = len(depq)
    
    if n == 0:
        raise IndexError

    elif n <= 2:
        return depq.pop()
    
    result = depq[1]
    
    depq[1] = depq.pop()
    
    n -= 1
    cur = 0
    limit = (n-1) >> 1

    while cur < limit:
        left = (cur<<1) + 1
        right = left + 1
        max_node = cur

        if (left<<1) < n and max(depq[(left<<1):(left<<1)+2]) > max(depq[(max_node<<1):(max_node<<1)+2]):
            max_node = left
        
        if (right<<1) < n and max(depq[(right<<1):(right<<1)+2]) > max(depq[(max_node<<1):(max_node<<1)+2]):
            max_node = right
        
        if max_node != cur:
            max_index = max_node << 1
            i = 1 if max_index+1 < n else 0

            temp = depq[max_index+i]
            depq[max_index+i] = depq[(cur<<1)+1]
            depq[(cur<<1)+1] = temp

            if max_index+1 < n and depq[max_index] > depq[max_index+1]:
                temp = depq[max_index]
                depq[max_index] = depq[max_index+1]
                depq[max_index+1] = temp
            
            cur = max_node
        
        else:
            break

    return result
    

result = []
t = int(sys.stdin.readline())

for _ in range(t):
    depq = []
    k = int(sys.stdin.readline())
    
    for i in range(k):
        op, num = sys.stdin.readline().split()

        if op == 'I':
            depq_push(depq, int(num))
        
        elif op == 'D':
            if len(depq) == 0:
                continue
            
            elif num == '1':
                depq_pop_max(depq)
            
            elif num == '-1':
                depq_pop_min(depq)

    if len(depq) == 0:
        result.append('EMPTY')
    else:
        result.append(f'{max(depq[0:2])} {min(depq[0:2])}')

for line in result:
    print(line)
