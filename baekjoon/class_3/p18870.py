n = int(input())
nums = list(map(int, input().split()))
nums_s = sorted(nums)
compress = {}

i = 0
for num in nums_s:
    if num in compress:
        continue
    compress[num] = i
    i += 1

last_num = nums.pop()
for num in nums:
    print(compress[num], end=' ')
print(compress[last_num])