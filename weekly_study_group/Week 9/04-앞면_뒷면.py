# 약수가 홀수개인 경우: 제곱수일 때
# N의 제곱근을 구하면 N 이하의 자연수에 몇 개의 제곱수가 있는지 확인 가능
from math import sqrt

N = int(input())
print(int(sqrt(N)))