# 제일 바깥쪽 동전부터 훑어보면서 동전의 면이 달라지는 구간을 선택하여 뒤집음
# 그 뒤집은 구간 안에서 같은 과정 반복 -> 재귀 이용
# coins: 0, 1로 구성된 문자열
def flip_coins(coins):
    # 왼쪽 바깥이 0으로 시작되는 경우 1이 나오는 구간을 찾음
    if coins.startswith('0'):
        # 1이 나오는 구간 시작점 초기화, 만약 1이 나오는 구간이 없는 경우 -1이 유지됨
        start = -1 
        # 1이 나오는 구간 시작점 탐색
        for i in range(len(coins)):
            if coins[i] == '1':
                start = i
                break
        # 1이 없는 경우 뒤집을 필요가 없으므로 0회
        if start == -1:
            return 0
        # 1이 나오는 구간을 뒤에서부터 탐색
        for i in reversed(range(len(coins))):
            if coins[i] == '1':
                end = i
                break
        # 1로 시작되고 끝나는 구간에 대해서 1회 뒤집고 그 안에서 같은 과정 반복
        return 1 + flip_coins(coins[start:end+1])
    # 왼쪽 바깥이 1로 시작되는 경우 같은 과정을 0과 1을 서로 바꾸어 실행함
    else:
        start = -1
        for i in range(len(coins)):
            if coins[i] == '0':
                start = i
                break
        if start == -1:
            return 0
        
        for i in reversed(range(len(coins))):
            if coins[i] == '0':
                end = i
                break
        return 1 + flip_coins(coins[start:end+1])
        
print(flip_coins(input()))