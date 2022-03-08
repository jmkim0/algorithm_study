def nqueen(matrix, y):
    n = len(matrix)
    result = 0

    for x in range(n):
        if not col_chk[x] and not diag_chk1[x+y] and not diag_chk2[y-x]:
            if y == n-1:
                result += 1
            else:
                col_chk[x] = True
                diag_chk1[x+y] = True
                diag_chk2[y-x] = True
                matrix[y][x] = 1
                result += nqueen(matrix, y+1)
                col_chk[x] = False
                diag_chk1[x+y] = False
                diag_chk2[y-x] = False
                matrix[y][x] = 0
    
    return result

N = int(input())
if N == 1:
    print(1)
else:
    col_chk = [False] * N
    diag_chk1 = [False] * (N*2-1)
    diag_chk2 = [False] * (N*2-1)
    matrix = [[0]*N for _ in range(N)]
    result = 0
    mid = N // 2
    for x in range(mid):
        col_chk[x] = True
        diag_chk1[x] = True
        diag_chk2[-x] = True
        matrix[0][x] = 1
        result += nqueen(matrix, 1)
        col_chk[x] = False
        diag_chk1[x] = False
        diag_chk2[-x] = False
        matrix[0][x] = 0
    result *= 2
    if N%2 == 1:
        col_chk[mid] = True
        diag_chk1[mid] = True
        diag_chk2[-mid] = True
        matrix[0][mid] = 1
        result += nqueen(matrix, 1)
    print(result)
