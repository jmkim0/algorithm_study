a, b, c = map(int, input().split(' '))

# print(pow(a, b, c)) # 파이썬 기본함수로도 빠르게 계산 가능 (아마도 더)

# divide and conquer로 exp를 2로 나눠가면서 계산해봄 O(n) -> O(log n) 기대
# 추가로 base의 크기가 mod보다 큰 경우 미리 mod를 취해서 곱셈 연산 자체의 시간을 줄이도록 기대함
def pow_mod(base, exp, mod):
    if mod == 1:
        return 0
    if base > mod:
        base %= mod
    if base == 1:
        return 1
    if exp == 1:
        return base
    if exp%2:
        return (pow_mod(base, exp//2, mod)**2 * base) % mod
    else:
        return pow_mod(base, exp//2, mod)**2 % mod

print(pow_mod(a, b, c))