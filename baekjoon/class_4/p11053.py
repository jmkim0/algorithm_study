N = int(input())
A = list(map(int, input().split()))

# l = 0
# m = [0] * (N+1)

# for i in range(0, N):
#     lo = 1
#     hi = l + 1
#     while lo < hi:
#         mid = (hi+lo) // 2
#         if A[m[mid]] < A[i]:
#             lo = mid + 1
#         else:
#             hi = mid
    
#     nl = lo

#     m[nl] = i
    
#     if nl > l:
#         l = nl

# print(l)

# DP
result = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if A[i] > A[j] and result[i] < result[j] + 1:
            result[i] = result[j] + 1
            
print(max(result))
    
