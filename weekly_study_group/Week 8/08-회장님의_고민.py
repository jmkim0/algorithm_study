N = int(input())
brs = tuple(map(int, input().split())) # budget requests
M = int(input())

if sum(brs) <= M:
    print(max(brs))
else:
    def get_total(limit):
        total = 0
        for br in brs:
            if br >= limit:
                total += limit
            else:
                total += br
        return total

    lo = M // N
    hi = 100000
    while lo < hi:
        mid = (lo+hi) // 2
        if get_total(mid) < M:
            lo = mid + 1
        else:
            hi = mid

    if get_total(lo) == M:
        print(lo)
    else:
        print(lo-1)
    