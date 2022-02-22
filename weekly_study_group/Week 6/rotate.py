class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        mid = n // 2
        for i in range(mid):
            for j in range(mid + n%2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[-j-1][i]
                matrix[-j-1][i] = matrix[-i-1][-j-1]
                matrix[-i-1][-j-1] = matrix[j][-i-1]
                matrix[j][-i-1] = temp

                # matrix[i][j], matrix[-j-1][i], matrix[-i-1][-j-1], matrix[j][-i-1] = matrix[-j-1][i], matrix[-i-1][-j-1], matrix[j][-i-1], matrix[i][j]
                # 원소 하나하나를 넣는 방식이 배열(tuple, list 등 iterable)로 한번에 넣는 것보다 빠르고 메모리도 살짝 적게 먹음 (단순 변수와 object의 크기 차이)

sol = Solution()
n = 22
a = [[chr(i+ord('A'))] * n for i in range(n)]
for row in a:
    print(*row)
print("-" * n*2)
sol.rotate(a)
for row in a:
    print(*row)