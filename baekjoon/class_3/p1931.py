import sys

n = int(sys.stdin.readline())
meetings = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

meetings.sort(key=lambda x: (x[1], x[0])) # 회의의 시작시간과 종료시간이 같을 수 있어서 시작시간이 빠른 순서대로도 정렬해야함

endtime = 0
count = 0
for m in meetings:
    if endtime <= m[0]:
        endtime = m[1]
        count += 1

print(count)