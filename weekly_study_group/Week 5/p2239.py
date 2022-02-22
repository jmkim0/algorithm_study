# Python 3: 32124 KB / 5940 ms
# PyPy3: 136468 KB / 1580 ms

import sys
from collections import deque


# 해당 행, 열, 3x3 사각형에 해당 숫자가 존재하는지 체크하는 list들
# row_chk[row][num]: row번째 행에 num이라는 숫자가 이미 존재하면 True, 없으면 False
# col_chk[row][num]: col번째 열에 num이라는 숫자가 이미 존재하면 True, 없으면 False
# box_chk[row][num]: box번째 3x3사각형에 num이라는 숫자가 이미 존재하면 True, 없으면 False
#                    위에서부터 오른쪽으로 세서 1~9의 번호를 붙임, box = row//3 * 3 + col//3
row_chk = [[False]*10 for _ in range(9)]
col_chk = [[False]*10 for _ in range(9)]
box_chk = [[False]*10 for _ in range(9)]

# 빈 칸의 좌표를 담을 deque, (row, col) 형태로 오름차순으로 넣음
# 초기화할 때는 뒤로 순서대로 넣고 문제를 풀 때는 앞에서부터 빼내야 해서 deque를 사용함
dq = deque()


# matrix: 스도쿠 보드를 나타내는 2-d list
# row_chk, col_chk, box_chk, dq를 초기화하는 함수
def init(matrix):
    for i in range(9):
        for j in range(9):
            num = matrix[i][j]
            
            if num != 0:
                row_chk[i][num] = True
                col_chk[j][num] = True
                box_chk[i//3 * 3 + j//3][num] = True
            else:
                dq.append((i, j))


# 백트랙킹 방식으로 빈 칸 하나하나 숫자를 넣어가며 스도쿠를 푸는 함수
def solve(matrix):
    if not dq:
        return True

    row, col = dq[0]
    box = row//3 * 3 + col//3

    for i in range(1, 10):
        # 답일 수도 있는 경우
        if not row_chk[row][i] and not col_chk[col][i] and not box_chk[box][i]:
            # 일단 답으로 생각하고 값을 대입함
            matrix[row][col] = i
            row_chk[row][i] = True
            col_chk[col][i] = True
            box_chk[box][i] = True
            dq.popleft()
            
            # 정답으로 판명되면 True가 연쇄적으로 반환됨
            if solve(matrix):
                return True
            
            # 오답으로 판명되면 뒤로 돌아감
            matrix[row][col] = 0
            row_chk[row][i] = False
            col_chk[col][i] = False
            box_chk[row//3 * 3 + col//3][i] = False
            dq.appendleft((row, col))

    return False


# main
matrix = [list(map(int, sys.stdin.readline().strip())) for _ in range(9)]

init(matrix)
solve(matrix)

for line in matrix:
    print(''.join(map(str, line)))

