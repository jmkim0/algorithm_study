a, b, c = map(int, input().split())

# print(pow(a, b, c))

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