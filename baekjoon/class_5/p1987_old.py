import sys

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def dfs(matrix, y, x, visited, v_letter):
    result = 0

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if ny < 0 or nx < 0 or ny >= r or nx >= c or visited[ny][nx]:
            continue
        
        letter_i = ord(matrix[ny][nx]) - ord('A')

        if v_letter[letter_i]:
            continue

        visited[ny][nx] = True
        v_letter[letter_i] = True
        result = max(result, dfs(matrix, ny, nx, visited, v_letter))

        if result == 26:
            return 26
        
        visited[ny][nx] = False
        v_letter[letter_i] = False

    return result + 1


r, c = map(int, sys.stdin.readline().split())
matrix = [sys.stdin.readline().strip() for _ in range(r)]
visited = [[False]*c for _ in range(r)]
v_letter = [False] * 26
visited[0][0] = True
v_letter[ord(matrix[0][0]) - ord('A')] = True

print(dfs(matrix, 0, 0, visited, v_letter))