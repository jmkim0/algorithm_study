from math import factorial


# elice상 python 버전이 낮아 math.comb이 없어서 math.factorial을 이용하여 정의해줌 
def comb(n, k):
    if 2*k > n:
        return comb(n, n-k)
    else:
        product = 1
        for i in range(n-k+1, n+1):
            product *= i
        return product // factorial(k)

# 1
# https://mathworld.wolfram.com/PowerSum.html (20) 참고
# 함수 내에 덧셈, 뺄셈, 곱셈만 존재하므로 각 항에 modulo를 취해도 결과가 같음
# pow 함수에 mod 매개변수 사용함
def power_sum_mod(base, exponent, modulus):
    if base > exponent: # base가 exponent보다 큰 경우에 공식을 사용, loop수가 exponent에 비례하므로 base가 매우 커져도 상대적으로 시간이 적게 듬
        power_sum = 0
        for i in range(1, exponent+1):
            for j in range(i):
                term = pow(i - j, exponent, modulus) * comb(base + exponent - i + 1, base - i) * comb(exponent + 1, j)
                if j % 2 == 1:
                    power_sum -= term
                else:
                    power_sum += term
        return power_sum % modulus
    else: # base가 exponent보다 작은 경우 단순하게 계산, loop수가 base에 비례함
        return sum(pow(i, exponent, modulus) for i in range(1, base+1)) % modulus


# 2
# https://www.geeksforgeeks.org/sum-of-kth-powers-of-first-n-natural-numbers/ 참고
# function to return the sum of the kth
# powers of n natural numbers
# 함수 내에 나눗셈이 존재하여 나눗셈 전에는 modulo 적용 불가
# pow 함수에 mod 매개변수 사용 안함
def power_sum_mod2(n, k, mod):
	p = 0
	num1, temp = 1, 1
	arr = [1 for i in range(1000)]
	
	for j in range(1, k + 1):
		
		# when j is 1
		if j == 1:
			num1 = (n * (n + 1)) // 2
			
			# calculating sum(n^1) of unity powers
			#of n storing sum(n^1) for sum(n^2)
			arr[p] = num1
			p += 1
			
			# if k==1 then temp is the result
		else:
			temp = pow(n + 1, j + 1) - 1 - n
			
			# for finding sum(n^k) removing 1 and
			# n*KCk from (n+1)^k
			for s in range(1, j):
				
				# Removing all kC2 * sum(n^(k - 2))
				# + ... + kCk - 1 * (sum(n^(k - (k - 1))
				temp = temp - (arr[j - s - 1] *
							comb(j + 1, s + 1))
			temp = temp // (j + 1)
			
			# storing the result for next sum
			# of next powers of k
			arr[p] = temp
			p += 1
	temp = arr[p - 1]
	return temp % mod


n, k = map(int, input().split())

print(power_sum_mod(n, k, 1000000009))


# 이하 시간초과된 코드 목록

# 1
# print(sum(i**k for i in range(1, n+1)) % 1000000009)

# 2
# def modulo_pow(base, exponent, modulus):
#     if modulus == 1:
#         return 0;
#     else:
#         remainder = 1
#         for e in range(exponent):
#             remainder = remainder*base % modulus
#         return remainder

# remainder_sum = 0;
# for i in range(1,n+1):
#     remainder_sum += modulo_pow(i, k, 1000000009)

# print(remainder_sum % 1000000009)

# print(sum(pow(i, k, 1000000009) for i in range(1, n+1)) % 1000000009)

# 3
# remainder = 0
# for i in range(1, n+1):
#     remainder = (remainder + pow(i, k, 1000000009)) % 1000000009
# print(remainder)
