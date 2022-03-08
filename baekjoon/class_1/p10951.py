while True:
    try:
        a_b = input().split(" ")
        print(int(a_b[0]) + int(a_b[1]))
    except:
        break; # input이 없을 때 exception 발생하고 프로그램 종료