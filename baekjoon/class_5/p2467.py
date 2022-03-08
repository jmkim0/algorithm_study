N = int(input())
sol = tuple(map(int, input().split()))
lo = 0
hi = N-1
result = [sol[lo], sol[hi]]
while lo+1 < hi:
    if sol[lo] + sol[hi] > 0:
        hi -= 1
        if abs(sol[lo] + sol[hi]) < abs(sum(result)):
            result = [sol[lo], sol[hi]]
    elif sol[lo] + sol[hi] < 0:
        lo += 1
        if abs(sol[lo] + sol[hi]) < abs(sum(result)):
            result = [sol[lo], sol[hi]]
    else:
        break
print(*result)

'''
binary search를 중간에 섞어가면서 해서 linear한 탐색과정을 logarithmic하게 바꿀 수도 있어 보임
다만 여러 번 시행하면 worst case에서 O(n*log(n))이 될 가능성도 있어서 잘 생각해야될 것 같긴 함
- 산성과 알칼리성이 균형있게 분포된 경우 0에 가까운 pair가 [leftmost, rightmost]일 수 있는데
  단순 선택으로 O(1)에 가능한 것을 O(log(n))에 하게 될 수도 있음
그래서 최초에 0에 가장 가까운 pair를 찾는 과정에서나 사용하는게 제일 그나마 가능성있지 않나 싶음
- 산성과 알칼리성이 불균형하게 분포된 경우에는 최초의 불필요한 단순 탐색을 없앨 수 있을 듯함
- 극단적으로 생각했을 때 거의 산성으로만 또는 알칼리성으로만 존재하면 0에 가까운 pair가 왼쪽이나
  오른쪽에 몰려있을 수 있는데 단순탐색시 O(n)이 걸리지만 binary search는 O(log(n))이 걸림
여기선 하지 않고 2473번 문제에서 해보겠음
'''