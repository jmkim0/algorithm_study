# 32916KB / 892ms

import sys
from copy import deepcopy
from collections import deque

# dir: 방향을 나타내는 변수, 시계방향으로 위부터 0, 1, 2, 3
# dir 방향으로 1회 이동하는 함수
# 아무 변화가 없는 경우 -1 반환, 변화가 있는 경우 가장 큰 블록 반환
# matrix: 게임 보드를 나타내는 2-d list
def move_2048(matrix, dir):
    n = len(matrix)
    
    # 변화가 있는지 감지하는 flag
    changed = False
    
    if dir == 0 or dir == 2:
        if dir == 0:
            j_range = range(n)
        else:
            j_range = range(n-1, -1, -1)
        # 블록의 이동이 없는 축에 대해서 루프함
        for i in range(n):
            # 유의미한(0이 아닌) 블록만을 저장하는 임시 deque
            dq = deque()
            
            # 블록이 이동하는 축에서 유의미한 블록들만 dq에 순서대로 저장
            for j in j_range:
                if matrix[j][i] != 0:
                    dq.append(matrix[j][i])
            
            # 해당 축에 업데이트된 블록들을 채움
            for j in j_range:
                if dq:
                    temp = dq.popleft()
                    if dq and dq[0] == temp:
                        temp += dq.popleft()
                    if matrix[j][i] != temp:
                        matrix[j][i] = temp
                        changed = True
                else:
                    matrix[j][i] = 0

    elif dir == 1 or dir == 3:
        if dir == 3:
            j_range = range(n)
        else:
            j_range = range(n-1, -1, -1)
        
        # 블록의 이동이 없는 축에 대해서 루프함
        for i in range(n):
            # 유의미한(0이 아닌) 블록만을 저장하는 임시 deque
            dq = deque()
            
            # 블록이 이동하는 축에서 유의미한 블록들만 dq에 순서대로 저장
            for j in j_range:
                if matrix[i][j] != 0:
                    dq.append(matrix[i][j])
            
            # 해당 축에 업데이트된 블록들을 채움
            for j in j_range:
                if dq:
                    temp = dq.popleft()
                    if dq and dq[0] == temp:
                        temp += dq.popleft()
                    if matrix[i][j] != temp:
                        matrix[i][j] = temp
                        changed = True
                else:
                    matrix[i][j] = 0

    # 변화가 없는 경우 -1 반환
    if not changed:
        return -1
    # 변화가 있는 경우 최대 블록 반환
    else:
        return max(map(max, matrix))


# 2048 게임을 이동 제한 5회로 실행했을 때 최고 점수(최대 블록)을 반환하는 함수
def play_2048(matrix):
    # 초기 상태에서 가장 큰 블록으로 결과값을 초기화함
    result = max(map(max, matrix))
    
    backtrack = 5
    for dir0 in range(4):
        for dir1 in range(4):
            for dir2 in range(4):
                for dir3 in range(4):
                    for dir4 in range(4):
                        temp_matrix = deepcopy(matrix)
                        dirs = [dir0, dir1, dir2, dir3, dir4]
                        
                        for i in range(5):
                            score = move_2048(temp_matrix, dirs[i])

                            if score == -1:
                                backtrack = i
                                break
                            elif result < score:
                                result = score
                        
                        if backtrack < 4:
                            break
                        backtrack = 5

                    if backtrack < 3:
                        break
                    backtrack = 5

                if backtrack < 2:
                    break
                backtrack = 5
            
            if backtrack < 1:
                break
            backtrack = 5

        backtrack = 5

    return result


n = int(sys.stdin.readline())
matrix = []

for i in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

print(play_2048(matrix))
