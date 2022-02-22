import sys

# 31^2 == 961 < 1000 < 32^2 == 1024이므로 
# 1부터 1000까지의 자연수들 중 31까지의 소수의 배수들을 제거하면 소수만 남는다
nums = [1] * 1000
nums[0] = 0

for i in range(2, 32):
    if nums[i-1]:
        temp = i * 2
        
        while temp <= 1000:
            nums[temp-1] = 0
            temp += i

n = int(sys.stdin.readline())
n_iter = map(int, sys.stdin.readline().split())
result = 0

for num in n_iter:
    result += nums[num-1]

print(result)