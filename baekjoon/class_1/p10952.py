while True:
    a_b = input().split(" ")
    if a_b[0] == "0" and a_b[1] == '0':
        break
    print(int(a_b[0]) + int(a_b[1]))