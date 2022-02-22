import sys

r, c = map(int, sys.stdin.readline().split())
matrix = []
letters = set()

for _ in range(r):
    line = sys.stdin.readline().strip()
    matrix.append(line)
    letters |= set(line) # |: union

len_limit = len(letters)
max_len = 1
s = [(0, 0, matrix[0][0])] # stack 사용 (dfs)
visited = [['']*c for _ in range(r)]

while s:
    y, x, path = s.pop()
    
    # list를 사용하여 index를 iterate하는 구조보다 tuple이 직접 iterate하는 구조가 훨씬 빠름
    # python처럼 iterator를 쉽게 만드는 경우가 아니면 배열 + index 구조를 써야할 것 같긴 함
    for dy, dx in (1, 0), (0, 1), (-1, 0), (0, -1): 
        ny = y + dy
        nx = x + dx

        if 0 <= ny < r and 0 <= nx < c and matrix[ny][nx] not in path:
            new_path = path + matrix[ny][nx]
            max_len = max(max_len, len(new_path))

            if max_len == len_limit:
                break
            
            if visited[ny][nx] != new_path: # 중복체크
                s.append((ny, nx, new_path))
                visited[ny][nx] = new_path
        
    if max_len == len_limit:
        break

print(max_len)