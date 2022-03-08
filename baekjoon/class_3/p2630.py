import sys

def count_paper(matrix):
    n = len(matrix)

    if n == 1:
        return (1-matrix[0][0], matrix[0][0])

    mid = n // 2
    w1, b1 = count_paper([line[:mid] for line in matrix[:mid]])
    w2, b2 = count_paper([line[mid:] for line in matrix[:mid]])
    w3, b3 = count_paper([line[:mid] for line in matrix[mid:]])
    w4, b4 = count_paper([line[mid:] for line in matrix[mid:]])

    w = w1 + w2 + w3 + w4
    b = b1 + b2 + b3 + b4
    if (w, b) == (4, 0):
        return (1, 0)
    elif (w, b) == (0, 4):
        return (0, 1)
    else:
        return (w, b)

n = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

w, b = count_paper(matrix)
print(w)
print(b)