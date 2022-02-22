cheetahs = input()

# 순서대로 나가고 들어오는 것으로 생각

stack = [] # 나가있는 치타를 저장하는 리스트
out_check = {} # 치타가 나갔는지 체크, stack 리스트를 순회하는 것보다 빠르도록 딕셔너리 이용
for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    out_check[c] = False
# stack_overlapped = []
result = 0


for cheetah in cheetahs:
    if not out_check[cheetah]: # 치타가 아직 나간적이 없음
        stack.append(cheetah)
        out_check[cheetah] = True
    elif stack[-1] == cheetah: # 마지막으로 나간 치타가 들어옴
        stack.pop()
    else: # 자기보다 일찍 나가서 아직 안 들어온 치타 수 = 경로가 겹치는 수
        i = 1 
        while stack[-1-i] != cheetah:
            i += 1
        result += i
        stack.pop(-1-i)
        
# list.pop(index)를 사용하지 않고 stack을 2개 사용한 방법
# 시간복잡도도 별 차이 없고 공간복잡도만 확실히 늘어나는 것 같아서 버림
#         while stack:
#             stack_overlapped.append(stack.pop())
#             result += 1
#             if stack[-1] == cheetah:
#                 stack.pop()
#                 break
#         while stack_overlapped:
#             stack.append(stack_overlapped.pop())

print(result)
        