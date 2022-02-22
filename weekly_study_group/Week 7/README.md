11주차 스터디
===
[난이도 하] 문제들
---
대부분 쉽게 풀려서 따로 언급할 게 없는 것 같습니다.  
입력 사이즈들도 다 작아서 특이하게 구현한 것도 없습니다.

<br>

[난이도 중] 너가 왜 거기서 나와?
---
### 구현한 방법  
N의 형태를 보고 계산할 수 있는 방법이 있는지 생각해봤는데 패턴이 너무 다양할 수 있어서 거르고 '새로운 수'를 문자열로 만들어가면서 언제 처음 나타나는지 찾도록 했습니다.  
처음부터 N까지 모든 숫자를 합친 문자열을 만들지 않고 확인하는 위치에 따라 N의 자리수에 맞게 문자열을 늘립니다.
### 시간복잡도? 공간복잡도?  
N까지 문자열로 합치기 전에 웬만하면 끝나는 것 같아서 실제 시간복잡도가 어떨 지는 잘 모르겠습니다.  
N의 자리수는 $`O(log N)`$의 공간복잡도이고 N까지 문자열로 합친 경우의 '새로운 수'의 길이는 $`O(Nlog N)`$의 공간복잡도입니다.  
만약 N까지 문자열로 합쳐서 비교한다고 하면 시간복잡도가 $`O(N(log N)^2)`$일 수 있습니다.

<br>

[난이도 중] 둘이서 만든 수
---
### 주의
5번 입력에 이슈가 있어서 수정되었으니 예전에 제출했을 때 오답이었으면 다시 제출해보세요!  
### 구현한 방법
~~A, B의 모든 부분합을 key로 하고 그 경우의 수를 value로 하는 dict를 만들어서 항목 수가 더 적은 dict에 대해서 루프하고 원하는 T값을 만들 수 있는 경우의 수를 다 더하도록 했습니다.~~  
A의 모든 부분합을 key로 하고  그 경우의 수를 value로 하는 dict를 만든 후 B의 모든 부분합을 구할 때 원하는 T값을 만들 수 있는지 바로 확인하는 방법으로 바꿨습니다.  
쓸 데 없이 시간을 더 쓸 필요가 없었군요 😅
### 시간복잡도? 공간복잡도?
A의 부분합 dict는 $`O(N^2)`$의 시간복잡도로 만들고 최악의 경우--겹치는 부분합이 없는 경우--공간복잡도도 $`O(N^2)`$입니다.  
B의 부분합을 구하면서 경우의 수를 계산하는데에 추가로 $`O(M^2)`$의 시간복잡도가 걸립니다.  
총 시간복잡도는 $`O(N^2 + M^2)`$, 총 공간복잡도는 $`O(N^2)`$입니다.


<br>

[난이도 중] 문자열 압축
---
### 주의
5번 입력에 이슈가 있어서 수정되었으니 예전에 제출했을 때 오답이었으면 다시 제출해보세요! 
### 구현한 방법
스택을 사용해서 괄호가 끝까지 닫힌 경우를 찾고 그 안의 문자열에 대해 압축해제하는 과정을 재귀함수를 이용하여 반복합니다.  
memoization을 사용하여 혹시나 같은 문자열이 들어오는 경우 더 빠르게 작동할 수 있도록 했습니다.
### 시간복잡도? 공간복잡도?
괄호가 많은 경우 시간복잡도가 $`O(N^2)`$에 가까울 수 있을 것 같습니다.  
공간복잡도는 memoization이 없다면 $`O(1)`$이고 있다면 최악의 경우 $`O(N)`$일 것 같습니다.

<br>

[난이도 상] 광부 도도새
---
[0826] 실시간 문제풀이 특강에서 다룬 문제입니다.  
[GitLab](https://yeardream-gitlab.elice.io/test-answer/special/-/blob/main/%5B0826%5D%20%EA%B9%80%EA%B2%BD%EB%AF%BC%20%EA%B0%95%EC%82%AC%EB%8B%98%20%ED%8A%B9%EA%B0%95%20%EC%9E%90%EB%A3%8C/03_%EA%B4%91%EB%B6%80%20%EB%8F%84%EB%8F%84%EC%83%88.py)에도 업로드되어 있네요.

<br><br>

???
===
[난이도 중] 체셔의 3의 배수 혐오
---
### 구현한 방법
각 숫자를 3으로 나눴을 때 나오는 나머지에 따라 분류하고 인접하지 않게 배열합니다.  
3의 배수는 서로 인접할 수 없고 나머지가 1인 수와 나머지가 2인 수는 서로 인접할 수 없습니다.  
비둘기집 원리를 생각해서 불가능한 경우를 걸러냅니다.  
### 시간복잡도? 공간복잡도?
시간복잡도는 정렬 이상의 복잡한 연산이 없기 때문에 $`O(Nlog N)`$ 입니다.  
공간복잡도는 각 수를 분류할 때 필요한 공간이 있어서 $`O(N)`$입니다.
### 맞왜틀?
5번 입력만 오답이 나오는데 왜 그런지 잘 모르겠습니다.  
테스트를 많이 해보지는 않았는데 사전순 정렬 부분이 문제가 아닌가 싶긴 합니다.  

<br>

[난이도 상] 자리 바꾸기
---
### 구현한 방법
~~숫자 중 맨 앞에 왔을 때 더 큰 수를 만드는 그 숫자를 '최대값'으로 정하고 이를 탐색해서 맨 앞에 세우는 과정을 반복합니다.  
'최대값'은 다음과 같이 비교해서 정해집니다.~~  
```
nums[i] + max_val < max_val + nums[i]
```
~~두 수의 위치를 바꿔가면서 문자열로 합친 후 비교하면 어떤 수를 앞에 배열해야 더 큰 수가 되는지 알 수 있습니다.~~  
반례가 있었습니다.  
- 입력
``` 
5
11 8 99 999 1
3
```
- 올바른 출력
```
999118991
```
- 내 출력
```
991189991
```
~~'최대값'을 정할 때 `nums[i]*6 > max_val*6` 로 비교하도록 바꾸어봤습니다. (nums: List[str], max_val: str)~~  
[횟수 상관없이 최대가 되는 경우를 구하는 방법](https://rosettacode.org/wiki/Largest_int_from_concatenated_ints#Python)은 찾아볼 수 있었는데 횟수 제한이 있으니 잘 모르겠네요.
### 시간복잡도? 공간복잡도?
?

<br>