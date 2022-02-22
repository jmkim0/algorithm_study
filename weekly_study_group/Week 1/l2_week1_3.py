# 1
# n = int(input())

# nth_record = str(2 ** n)

# digit_sum = 0

# for digit in nth_record:
#     digit_sum += int(digit)
    
# print(digit_sum)

# 2
# print(sum([int(x) for x in str(2 ** int(input()))]))

# 3
# print(sum(map(int, str(2 ** int(input())))))

# 4
n = int(input())

nth_record = 2 ** n
digit_sum = 0
while nth_record:
    digit_sum, nth_record = digit_sum + nth_record%10, nth_record // 10

print(digit_sum)
