n = int(input())
score_list = []

for i in range(n):
    result = input()
    count_o = 0
    score = 0

    for char in result:
        if char == 'O':
            count_o += 1
            score += count_o
        else:
            count_o = 0

    score_list.append(score)

for score in score_list:
    print(score)
