import sys
from itertools import permutations

def sudoku_helper(matrix, row, is_blank, nums_to_fill):
    blanks = len(nums_to_fill[row])
    
    if blanks == 0:
        if row == 8:
            return True
        else:
            return sudoku_helper(matrix, row+1, is_blank, nums_to_fill)
    
    row_box = row//3 * 3
    
    bt = {}

    for p in permutations(nums_to_fill[row]):
        if bt and p[:cur+1] in bt:
            continue

        cur = 0
        
        for i in range(9):
            if not is_blank[row][i]:
                continue
            
            if p[cur] in [matrix[j][i] for j in range(9)]:
                break

            col_box = i//3 * 3
            
            box = matrix[row_box][col_box:col_box+3] + matrix[row_box+1][col_box:col_box+3] + matrix[row_box+2][col_box:col_box+3]
            if p[cur] in box:
                break
            
            matrix[row][i] = p[cur]
            cur += 1

            if cur == blanks:
                break

        if cur != blanks:
            bt[p[:cur+1]] = True
            for i in range(9):
                if is_blank[row][i]:
                    matrix[row][i] = '0'
            continue

        if row == 8:
            return True
        elif sudoku_helper(matrix, row+1, is_blank, nums_to_fill):
            return True
        else:
            for i in range(9):
                if is_blank[row][i]:
                    matrix[row][i] = '0'

    return False


def sudoku(matrix):
    is_blank = [[True if matrix[row][i] == '0' else False for i in range(9)] for row in range(9)]
    nums_to_fill = [[i for i in '123456789' if i not in matrix[row]] for row in range(9)]

    return sudoku_helper(matrix, 0, is_blank, nums_to_fill)


# main
matrix = [
    list(sys.stdin.readline().strip())
    for _ in range(9)
]

sudoku(matrix)

for line in matrix:
    print(''.join(line))

