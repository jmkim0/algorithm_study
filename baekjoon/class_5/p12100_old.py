import sys
from itertools import product
from copy import deepcopy


def play_2048(matrix):
    n = len(matrix)
    result = max(map(max, matrix))

    for moves in product(range(4), repeat=5):
        temp_matrix = deepcopy(matrix)

        for dir in moves:
            temp = move_2048(temp_matrix, dir)
            if temp == -1:
                break
            else:
                result = max(result, temp)

    return result


# dir: 방향을 나타내는 변수, 시계방향으로 0, 1, 2, 3
def dir_index_helper(dir, i, j):
    if dir == 0:
        return (j, i)
    if dir == 1:
        return (i, -1-j)
    if dir == 2:
        return (-1-j, i)
    if dir == 3:
        return (i, j)


def align_matrix(matrix, dir):
    n = len(matrix)
    changed = False
    
    for i in range(n):
        temp = []
        
        for j in range(n):
            y, x = dir_index_helper(dir, i, j)
            if matrix[y][x] != 0:
                temp.append(matrix[y][x])
        
        k = len(temp)

        if k == n:
            continue

        for j in range(k):
            y, x = dir_index_helper(dir, i, j)
            if matrix[y][x] != temp[j]:
                changed = True
                matrix[y][x] = temp[j]
        
        for j in range(k, n):
            y, x = dir_index_helper(dir, i, j)
            matrix[y][x] = 0
    
    return changed


dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]


def move_2048(matrix, dir):
    n = len(matrix)
    
    changed = False

    if align_matrix(matrix, dir):
        changed = True
    
    for i in range(n):
        for j in range(n-1):
            y, x = dir_index_helper(dir, i, j)

            if matrix[y][x] == 0:
                continue

            ny = y + dy[dir]
            nx = x + dx[dir]

            if matrix[y][x] == matrix[ny][nx]:
                matrix[y][x] *= 2
                matrix[ny][nx] = 0
                changed = True
    
    if align_matrix(matrix, dir):
        changed = True
   
    if not changed:
        return -1
    else:
        return max(map(max, matrix))


n = int(sys.stdin.readline())
matrix = []

for i in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

print(play_2048(matrix))
