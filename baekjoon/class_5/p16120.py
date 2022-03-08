import sys

# 글자수를 3으로 나눴을때 나머지가 1이 아니면 NP (P 자리에 PPAP를 넣으면 3글자씩 늘어남)
# - 이 경우는 채점에 큰 영향은 없는 것 같음, 어차피 테스트케이스가 다 피해가는 듯
# - 랜덤한 케이스로 생각하면 2/3는 미리 거르니까 의미는 있을 듯?
# 한 글자씩 stack에 넣되 A를 만나면 앞 뒤 글자를 없애는 방식
# 만약 A가 연속으로 있다면 무조건 NP
# stack에 P가 2개 이상 들어있지 않았을 때 A를 만나도 NP
def chk_ppap(ppap_str):
    s = []
    skip = False # A가 스택에 들어왔을 때 다음 글자는 스택에 넣지 않고 스킵하기 위한 flag
                 # A를 스택에 넣어놓고 확인하는 방법보다 조금 더 빠름
    
    if len(ppap_str)%3 != 1:
        return False

    for char in ppap_str:
        if skip: # 직전 글자가 A였던 경우
            if char == 'A': # A가 연속으로 나오는 경우
                return False
            skip = False
            continue
        if char == 'A':
            if len(s) <= 1: # stack에 최소 P 2개가 있어야 함
                return False
            s.pop()
            skip = True
        else:
            s.append(char)
    
    if skip: # 마지막 글자가 A인 경우
        return False

    if len(s) == 1 and s[0] == 'P': # PPAP라면 스택에는 P 1개만 남게 됨
        return True
    
    return False

ppap_str = sys.stdin.readline().strip()

print('PPAP' if chk_ppap(ppap_str) else 'NP')