S = input()

# memoization dict
s_dict = {'': 0}

# 재귀를 위한 함수 정의
# 문자열을 인자로 하고 압축해제한 문자열의 길이를 반환함
def decompress(s):
    if s in s_dict:
        return s_dict[s]
    n = len(s)
    result = 0
    stack = [] # 괄호를 담는 스택
    start = -1 # 괄호가 시작된 index
    end = -1 # 괄호가 끝난 index
    for i in range(n):
        # 괄호가 열리면 스택에 저장
        if s[i] == '(':
            stack.append(i)
        # 괄호가 닫히면 스택에서 빼냄
        # 스택이 비었으면 괄호가 정상적으로 모두 닫힌 것
        # - 그 괄호 안에 있는 문자열에 대해 압축해제
        # 마지막으로 만난 괄호의 끝부터 이번 괄호의 시작 사이에 있는 압축되지 않은 문자열 길이도 계산
        elif s[i] == ')':
            start = stack.pop()
            if not stack:
                result += start-end-2
                end = i
                result += int(s[start-1]) * decompress(s[start+1:end])
    # 마지막 괄호 이후로 있는 압축되지 않은 문자열 길이 계산
    result += n - end - 1
    s_dict[s] = result # memoization
    return result

print(decompress(S))