import sys

r, c = map(int, sys.stdin.readline().split())
matrix = []
letters = set() # 등장하는 모든 자모 set

for _ in range(r):
    line = sys.stdin.readline().strip()
    matrix.append(line)
    letters |= set(line) # |: union

len_limit = len(letters) # 경로의 길이가 등장하는 모든 자모 개수보다 클 수는 없음
max_len = 1
s = [(0, 0, matrix[0][0])] # stack 사용 (dfs), element: (y, x, path)
visited = [['']*c for _ in range(r)] # path 중복체크용, (0, 0)에 다시 올 일이 없어서 따로 초기화 X
# stack대신 set를 사용한다면 중복체크를 자동으로 할 수 있으나 
# - 순서가 엉켜서 len_limit에 도달하여 빠르게 종료되는 case에서는 살짝 더 느릴 수 있음
# queue(bfs)를 사용해도 중복체크만 따로 잘 되면 큰 상관은 없을 것 같음(어차피 모든 경우를 고려해야 함)
# - 다만 최대값에 도달하는 시간이 제일 느릴 수 밖에 없음.

while s:
    y, x, path = s.pop()
    
    # list를 사용하여 index를 iterate하는 구조보다 tuple이 iterate하는 구조가 훨씬 빠름
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