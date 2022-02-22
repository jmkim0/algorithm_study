N = int(input())
nums = list(map(int, input().split()))
S = int(input())

def swap(nums, start, s):
    if start == N-1 or s == 0:
        return ''.join(map(str, nums))
    
    if s >= N-1 - start:
        end = N
    else:
        end = start + s + 1
    
    max_val = nums[start] # '최대값'
    max_idx = start # '최대값'의 index
    
    # '최대값'과 그 index를 탐색
    for i in range(start+1, end):
        val = nums[i]
        if  val > max_val:
            max_val = val
            max_idx = i
    
    # '최대값'이 start위치로 오게 바꾸기 실행
    return swap(nums[:start] + [nums[max_idx]] + nums[start:max_idx] + nums[max_idx+1:], start + 1, s - (max_idx-start))

    
print(swap(nums, 0, S))

# 답은 맞을 수 밖에 없는 BFS
# from collections import deque

# N = int(input())
# nums = input().split()
# S = int(input())
# q = deque([(nums, 0)])
# result = ''.join(nums)

# while q:
#     cur_nums, s = q.popleft()
#     if s == S:
#         result = max(result, ''.join(cur_nums))
#         continue
#     changed = False
#     for i in range(N-1):
#         if cur_nums[i+1] + cur_nums[i] > cur_nums[i] + cur_nums[i+1]:
#             changed = True
#             q.append((cur_nums[:i] + [cur_nums[i+1], cur_nums[i]] + cur_nums[i+2:], s + 1))
#     if not changed:
#         result = max(result, ''.join(cur_nums))

# print(result)