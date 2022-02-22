N, S = map(int, input().split())
prices = map(int, input().split())

cumsum = [0]
temp = 0
for price in prices:
    temp += price
    cumsum.append(temp)
if cumsum[-1] < S:
    print(0)
else:
    done = False
    for i in range(1, N + 1):
        for j in range(N+1 - i):
            if cumsum[j + i] - cumsum[j] >= S:
                done = True
                break
        if done:
            print(i)
            break