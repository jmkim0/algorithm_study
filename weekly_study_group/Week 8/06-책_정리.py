N = int(input())
books = tuple(map(int, input().split()))

# LIS
M = [0] * (N+1)
l = 0

for i in range(N):
    lo = 1
    hi = l + 1
    while lo < hi:
        mid = (hi+lo) // 2
        if books[M[mid]] < books[i]:
            lo = mid + 1
        else:
            hi = mid
    M[lo] = i
    if lo > l:
        l = lo
print(N-l)