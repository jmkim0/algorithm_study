N = input()

i = 0
n = 1
num = ''

# N에 길이에 맞게 문자열을 늘리면서 어느 지점에 처음으로 N이 나타나는지 탐색
while True:
    while len(num) - i < len(N):
        num += str(n)
        n += 1
    if num[i:].startswith(N):
        print(i+1)
        break
    i += 1
    