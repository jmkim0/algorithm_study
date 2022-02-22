nums = input().split('0')

# X, Y: 0-9 자연수
if len(nums) == 1: # 10이 없는 경우, nums = ['XY']
    print(sum(map(int, nums[0])))
elif len(nums) == 3: # 10이 2개인 경우, nums == ['1', '1', '']
    print(20)
elif len(nums[0]) == 1: # 앞에 10이 있는 경우, nums == ['1', 'X']
    print(10 + int(nums[1]))
else: # 뒤에 10이 있는 경우, nums == ['X1', '']
    print(10 + int(nums[0][0]))
