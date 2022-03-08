n = int(input())
MOD = 1000000007

def fib(n, MOD):
	if n == 0:
		return (0, 1)
	else:
		a, b = fib(n//2, MOD)
		c = a * (b*2 - a)
		d = a*a + b*b
		if n % 2 == 0:
			return (c % MOD, d % MOD)
		else:
			return (d % MOD, (c+d) % MOD)

print(fib(n, MOD)[0])